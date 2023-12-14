import pandas as pd
import yaml

def load_credentials(file_path="credentials.yaml"):
    ''' 
    Load the credentials from the YAML file needed to load the AWS RDS database

    Paramaters: 
    - file_path (str): Path to the YAML file containing database credentials. Default is "credentials.yaml".

    Returns:
    credentials dict: A dictionary containing the database credentials.
    '''
    with open(file_path, "r") as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector:
    '''
    The RDSDatabaseConnector class represents the connection to the RDS database.

    Attributes:
    - credentials: The credentials needed to access the database.
    - engine: The SQLAlchemy engine used for database connection.

    '''
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.create_engine()
        ''' 
         Initialises the first instance of the RDSDatabaseConnector

        Parameters: 
        - credentials: The credentials needed to access the database.
        - engine: The SQLAlchemy engine used for database connection.
        '''
    def create_engine(self):
        ''' 
        Create and return a SQLAlchemy engine based on the provided credentials.

        Returns:
        sqlalchemy.engine.Engine: The SQLAlchemy engine.
        '''
        from sqlalchemy import create_engine

        db_url = f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        engine = create_engine(db_url)
        return engine

    def extract_data(self, table_name="loan_payments"):
        '''
        Extracts data from specified table in RDS database

        Paramaters:
        - table_name: The name of the table extracted from the database. Default here is set to "loan_payments".

        Returns:
        pandas.DataFrame: A DataFrame containing the extracted data.
        '''
        import pandas as pd

        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, self.engine)
        return df

    def save_to_csv(self, data_frame, file_name="loan_payments_data.csv"):
        '''
        Converts dataframe to .csv file.

        Paramaters:
        - data_frame: The dataframe that is to be saved.
        - file_name: The name given to the new .csv file.
        '''
        data_frame.to_csv(file_name, index=False)
        print(f"Data saved to {file_name}")

if __name__ == "__main__":
    credentials = load_credentials()
    rds_connector = RDSDatabaseConnector(credentials)
    data = rds_connector.extract_data()
    rds_connector.save_to_csv(data)

# Read the data from the csv file.
df = pd.read_csv("loan_payments_data.csv")
try:
    df = pd.read_csv("loan_payments_data.csv")
    print(df)
except FileNotFoundError:
    print("CSV file not found. Make sure the file path is correct.")
except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
except Exception as e:
    print(f"An error occurred: {e}")