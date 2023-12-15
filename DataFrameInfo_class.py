import pandas as pd

class DataFrameInfo:
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        return self.df.dtypes

    def extract_statistical_values(self):
        return self.df.describe()

    def count_distinct_values(self):
        return self.df.nunique()

    def print_shape(self):
        print("DataFrame Shape:", self.df.shape)

    def count_null_values(self):
        null_count = self.df.isnull().sum()
        percentage_null = (null_count / len(self.df)) * 100
        return pd.DataFrame({'Null Count': null_count, 'Percentage Null': percentage_null})