import pandas as pd 

class DataFrameTransform:
    def null_count_percentage (self):
        null_count = self.df.isnull().sum()
        percentage_null = (null_count / len(self.df)) * 100
        return pd.DataFrame({'Null Count': null_count, 'Percentage Null': percentage_null})
    
    def drop_columns(df, threshold=30):
        # Drop columns with missing values exceeding the threshold
        null_percentage = DataFrameTransform.null_percentage(df)
        columns_to_drop = null_percentage[null_percentage > threshold].index
        df = df.drop(columns=columns_to_drop)
        return df

    def impute_nulls(df, strategy='median'):
        # Impute missing values using median or mean
        if strategy == 'median':
            df = df.fillna(df.median())
        elif strategy == 'mean':
            df = df.fillna(df.mean())
        else:
            raise ValueError("Invalid imputation strategy. Choose 'median' or 'mean'.")
        return df