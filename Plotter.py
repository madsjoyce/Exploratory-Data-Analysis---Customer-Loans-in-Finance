import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class Plotter:

     def null_percentage(df):
        '''
        Works out percentage of null values

        Parameters:
        - df: pandas.DataFrame

        Returns:
        null_percentage
        '''
        null_percentage = (df.isnull().sum() / len(df)) * 100
        return null_percentage

     def plot_nulls(df):
        '''
        Plots null values on graph

        Paramaters:
        - df: pandas.DataFrame

        Returns:
        null_columns
        '''
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
        plt.title("Missing Values in DataFrame")
        plt.show()

     def columns_with_nulls(df):
       '''
       Finds column names with null values present

        Paramaters:
        - df: pandas.DataFrame

        Returns:
        null_columns
       '''
       null_columns = df.columns[df.isnull().any()]
       return null_columns


     def nulls_above_50_percent(df):
       '''
       Finds column names with null value presence over 50%

        Paramaters:
        - df: pandas.DataFrame   

        Returns:
        null_columns
       '''
       null_percentage = (df.isnull().sum() / len(df)) * 100
       columns_above_threshold = null_percentage[null_percentage > 50].index
       if not columns_above_threshold.empty:
         print(f"Columns with more than 50% null values: {columns_above_threshold}")
       else:
         print("No columns have more than 50% null values.")

     def identify_skewed_columns(df, skew_threshold=0.5):
       ''' 
       Identify skewed columns.
       
       Parameters:
       - df: pandas.DataFrame
       - skew_threshold: threshold at which data becomes too skewed.
       
       Returns:
       Skewed_columns 
       '''
       numeric_columns = df.select_dtypes(include=np.number).columns
       skewed_columns = df[numeric_columns].apply(lambda x: np.abs(x.skew()) > skew_threshold)
       return skewed_columns[skewed_columns].index.tolist()

     def apply_best_transformation(df, skewed_columns):
       for column in skewed_columns:
           if pd.api.types.is_numeric_dtype(df[column]):
               df[column] = np.log1p(df[column])
       return df

     def visualise_original_skewness(df, skewed_columns):
          """
          Visualise skewness of columns in the original DataFrame before transformations.

          Parameters:
           - df: original pandas.DataFrame
             Original DataFrame before transformations.
           - skewed_columns: list of str
            Columns identified as skewed.
           """
          plt.figure(figsize=(6, 6))
    
          # Visualise skewness before transformations
          sns.histplot(data=df[skewed_columns], kde=True)
          plt.title("Skewness Before Transformations")
    
          plt.show()

     def visualise_transformed_skewness(df, skewed_columns):
          """
          Visualise skewness of columns in the transformed DataFrame after transformations.

          Parameters:
          - df: transformed pandas.DataFrame
           DataFrame after transformations.
          - skewed_columns: list of str
          Columns identified as skewed.
          """
          plt.figure(figsize=(6, 6))
    
          # Visualize skewness after transformations
          sns.histplot(data=df[skewed_columns], kde=True)
          plt.title("Skewness After Transformations")
    
          plt.show()

     def visualise_boxplots(df):
          """
          Visualise boxplots for numerical columns in the DataFrame.

          Parameters:
          - df: pandas.DataFrame
          """
          numerical_columns = df.select_dtypes(include=['number']).columns

          plt.figure(figsize=(14, 8))
          df[numerical_columns].boxplot(sym='k.', notch=True, vert=False, patch_artist=True)
        
          plt.title("Boxplots for Numerical Columns")
          plt.xlabel("Values")
          plt.ylabel("Columns")
          plt.show()
      
     def visualise_heatmap(correlation_matrix):
        """
        Visualise heatmap for correlation matrix.

        Parameters:
        - correlation_matrix: pandas.DataFrame, correlation matrix
        """
        numerical_columns = correlation_matrix.select_dtypes(include=['number']).columns
        if not numerical_columns.empty:
            correlation_matrix_numerical = correlation_matrix[numerical_columns]

            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation_matrix_numerical, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
            plt.title("Correlation Matrix Heatmap (Numerical Data)")
            plt.show()
        else:
            print("No numerical columns to visualize.")