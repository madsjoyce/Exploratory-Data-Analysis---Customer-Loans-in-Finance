import pandas as pd

class DataTransform:
    '''
    Class transforms the datatype's of specific columns.
    '''
    
    def __init__(self, df):
        '''
        Initialises the DataTransform object.

        Parameters:
        - df (pd.DataFrame): The input DataFrame to be transformed.
        '''
        self.df = df

    def convert_to_numeric(self, columns):
        '''
        Convert specified columns to numeric format.

        Parameters:
        - columns: list of str, columns to be converted

        Returns:
        pandas.DataFrame
        '''

        self.df[columns] = self.df[columns].apply(pd.to_numeric, errors='coerce')
        return self.df

    def convert_to_datetime(self, columns):
        '''
        Convert specified columns to datetime format.

        Parameters:
        - columns: list of str, columns to be converted

        Returns:
        pandas.DataFram
        '''
      
        self.df[columns] = pd.to_datetime(self.df[columns], format="%b-%Y")
        return self.df

    def convert_to_categorical(self, columns):
        '''
        Convert specified columns to categorical format
        
        Parameters:
        - columns: list of str, columns to be converted
        Returns:
        pandas.DataFrame
        '''
        
        self.df[columns] = self.df[columns].astype('category')
        return self.df
    
    
    def remove_excess_symbols(self, columns):
        '''
        Remove excess symbols from specified columns.

        Parameters:
        - columns: list of str, columns to be processed

        Returns:
        pandas.DataFrame
        '''
        self.df[columns] = self.df[columns].str.extract('(\d+)', expand=False)
        self.df[columns] = self.df[columns].astype(float)
        return self.df

    def convert_to_boolean(self, columns):
        '''
        Convert specified columns to boolean format
        
        Parameters:
        - columns: list of str, columns to be converted

        Returns:
        pandas.DataFrame
        '''
        self.df[columns] = self.df[columns].astype(bool)
        return self.df
    
    def convert_categorical_to_numeric(self, columns):
        '''
        Convert categorical columns to numerical format
        
        Parameters:
        - columns: list of str, columns to be converted

        Returns:
        pandas.DataFrame
        '''
        self.df[columns], pd.factorize(self.df[columns])
        return self.df