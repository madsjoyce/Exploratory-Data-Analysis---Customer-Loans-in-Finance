import numpy as np

class DataFrameTransform:
    
    def null_percentage(df):
        """
        Calculate the percentage of missing values in each column of the DataFrame.

        Parameters:
        - df: pandas.DataFrame

        Returns:
        null_percentage: Percentage of missing values for each column.
        """        
        null_percentage = (df.isnull().sum() / len(df)) * 100
        return null_percentage
    
    def drop_columns(df, threshold=50):
        """
        Drop columns with missing values exceeding the specified threshold.

        Parameters:
        - df: pandas.DataFrame
        - threshold: percentage threshold for dropping columns (default: 50)

        Returns:
        pandas.DataFrame: DataFrame with specified columns dropped.
        """
        null_percentage = DataFrameTransform.null_percentage(df)
        columns_to_drop = null_percentage[null_percentage > threshold].index
        df = df.drop(columns=columns_to_drop)
        return df

    def impute_mean(df, columns=None):
        """
        Impute missing values with the mean value for specified columns in the DataFrame.

        Parameters:
        - df: pandas.DataFrame
        - columns: columns to impute (default: None)

        Returns:
        pandas.DataFrame: DataFrame with missing values imputed using the mean.
        """
        if columns is not None:
            if not set(columns).issubset(df.columns):
                raise ValueError("Invalid column names provided.")

            df[columns] = df[columns].fillna(df[columns].mean())
        else:
            pass

        return df

    def impute_median(df, columns=None):
        """
        Impute missing values with the median value for specified columns in the DataFrame.

        Parameters:
        - df: pandas.DataFrame
        - columns: columns to impute (default: None)

        Returns:
        pandas.DataFrame: DataFrame with missing values imputed using the median.
        """
        if columns is not None:
            if not set(columns).issubset(df.columns):
                raise ValueError("Invalid column names provided.")

            df[columns] = df[columns].fillna(df[columns].median())
        else:
            pass

        return df
    
    def impute_mode(df, columns=None):
        """
        Impute missing values with the mode value for specified columns in the DataFrame.

        Parameters:
        - df: pandas.DataFrame
        - columns: columns to impute (default: None)

        Returns:
        pandas.DataFrame: DataFrame with missing values imputed using the mode.
        """
        if columns is not None:
            if not set(columns).issubset(df.columns):
                raise ValueError("Invalid column names provided.")

            for column in columns:
                mode_value = df[column].mode().iloc[0]
                df[column] = df[column].fillna(mode_value)
        else:
            pass

        return df
    
    def remove_outliers(df, columns):
        """
        Remove outliers from specified columns in the DataFrame.

        Parameters:
        - df: pandas.DataFrame
        - columns:columns to remove outliers from

        Returns:
        pandas.DataFrame: DataFrame with outliers removed.
        """
        for column in columns:
            # Calculate IQR (Interquartile Range)
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1

            # Define the outlier bounds
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Remove outliers
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        return df

    def identify_highly_correlated_columns(df, threshold=0.8):
        """
        Identify highly correlated columns in the DataFrame.

        Parameters:
        - df: pandas.DataFrame
        - threshold: correlation threshold to consider

        Returns:
        List of tuples containing highly correlated column pairs.
        """
        numerical_columns = df.select_dtypes(include=['number'])
        if not numerical_columns.empty:
            mask = np.triu(np.ones_like(numerical_columns.corr(), dtype=bool), k=1)
            correlated_pairs = [
                (col1, col2) 
                for col1 in numerical_columns.columns 
                for col2 in numerical_columns.columns 
                if mask[numerical_columns.columns.get_loc(col1), numerical_columns.columns.get_loc(col2)] and abs(numerical_columns[col1].corr(numerical_columns[col2])) > threshold
                ]

            return correlated_pairs
        else:
            print("No numerical columns to identify correlations.")
            return []

    def remove_highly_correlated_columns(df, highly_correlated_columns):
        """
        Remove highly correlated columns from the DataFrame.

        Parameters:
        - df: pandas.DataFrame
        - highly_correlated_columns: highly correlated column pairs

        Returns:
        pandas.DataFrame: DataFrame with highly correlated columns removed.
        """
        for col1, col2 in highly_correlated_columns:
            # Decide which column to keep (e.g., based on domain knowledge or preference)
            # Here, we choose to keep col1
            df = df.drop(col2, axis=1, errors='ignore')

        return df