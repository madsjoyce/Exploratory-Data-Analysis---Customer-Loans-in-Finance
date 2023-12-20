import pandas as pd

class DataFrameInfo:

    '''
    A class for providing information and statistics about a pandas DataFrame.

    Parameters:
    - df: The pandas DataFrame.
    '''
    def __init__(self, df):
        """
        Initialises the DataFrameInfo object.

        Parameters:
        - df: The pandas DataFrame.
        """
        self.df = df

    def describe_columns(self):

        """
        Returns the data types of each column in the DataFrame.

        Returns:
        Data types of each column.
        """
        return self.df.dtypes

    def extract_statistical_values(self):
        """
        Returns basic statistical values for numeric columns in the DataFrame.

        Returns:
        Dataframe: Statistical values (count, mean, std, min, 25%, 50%, 75%, max) for numeric columns.
        """
        return self.df.describe()

    def count_distinct_values(self):
        """
        Returns the count of distinct values for each column in the DataFrame.

        Returns:
        Count of distinct values for each column.
        """
        return self.df.nunique()

    def print_shape(self):
        """
        Prints the shape (number of rows and columns) of the DataFrame.
        """
        print("DataFrame Shape:", self.df.shape)

    def count_null_values(self):
        """
        Returns a DataFrame containing the count and percentage of null values for each column.

        Returns:
        Count and percentage of null values for each column.
        """
        null_count = self.df.isnull().sum()
        percentage_null = (null_count / len(self.df)) * 100
        return pd.DataFrame({'Null Count': null_count, 'Percentage Null': percentage_null})