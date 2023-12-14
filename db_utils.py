
import yaml
import pandas as pd

# Step 3: Create a function to load credentials from credentials.yaml
def load_credentials(file_path="credentials.yaml"):
    with open(file_path, "r") as file:
        credentials = yaml.safe_load(file)
    return credentials

# Step 4: Create the RDSDatabaseConnector class
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.create_engine()

    # Step 5: Define a method to create an SQLAlchemy engine
    def create_engine(self):
        from sqlalchemy import create_engine

        # Create the database connection string
        db_url = f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        engine = create_engine(db_url)
        return engine

    # Step 6: Method to extract data as a Pandas DataFrame
    def extract_data(self, table_name="loan_payments"):
        import pandas as pd

        # Query the data from the specified table
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, self.engine)
        return df

    # Step 7: Method to save data to a local .csv file
    def save_to_csv(self, data_frame, file_name="loan_payments_data.csv"):
        data_frame.to_csv(file_name, index=False)
        print(f"Data saved to {file_name}")

# Example usage
if __name__ == "__main__":
    # Step 1: Load credentials
    credentials = load_credentials()

    # Step 4: Initialize RDSDatabaseConnector
    rds_connector = RDSDatabaseConnector(credentials)

    # Step 6: Extract data
    data = rds_connector.extract_data()

    # Step 7: Save data to local .csv file
    rds_connector.save_to_csv(data)

#import pandas as pd

df = pd.read_csv("loan_payments_data.csv")
print(df)