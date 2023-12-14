import pandas as pd

class DataTransform:
    '''
    Class transforms the datatype's of specific columns.
    '''
    
    def __init__(self, df):
        self.df = df

    @staticmethod
    def convert_to_numeric(self, columns):
        '''
        Convert specified columns to numeric format.

        Parameters:
        - df: pandas.DataFrame
        - columns: list of str, columns to be converted

        Returns:
        pandas.DataFrame
        '''

        self.df[columns] = self.df[columns].apply(pd.to_numeric, errors='coerce')
        return self.df

    @staticmethod
    def convert_to_datetime(self, columns):
        '''
        Convert specified columns to datetime format.

        Parameters:
        - df: pandas.DataFrame
        - columns: list of str, columns to be converted

        Returns:
        pandas.DataFram
        '''
      
        self.df[columns] = pd.to_datetime(self.df[columns], format="%b-%Y")
        return self.df

    @staticmethod
    def convert_to_categorical(self, columns):
        '''
        Convert specified columns to categorical format
        
        Parameters:
        - df: pandas.DataFrame
        - columns: list of str, columns to be converted
        Returns:
        pandas.DataFrame
        '''
        
        self.df[columns] = self.df[columns].astype('category')
        return self.df

    @staticmethod
    def remove_excess_symbols(self, columns):
        '''
        Remove excess symbols from specified columns.

        Parameters:
        - df: pandas.DataFrame
        - columns: list of str, columns to be processed

        Returns:
        pandas.DataFrame
        '''
        #for col in columns:
            #if df[col].dtype == 'O':  # Check if the column contains object (string) values
        self.df[columns] = self.df[columns].apply(DataTransform.extract_numeric_from_string)
        return self.df

    @staticmethod
    def convert_to_boolean(self, columns):
        self.df[columns] = self.df[columns].astype(bool)
        return self.df