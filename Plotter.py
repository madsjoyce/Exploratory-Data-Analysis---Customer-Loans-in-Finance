import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:

   def null_percentage(df):
        # Calculate the percentage of missing values in each column
        null_percentage = (df.isnull().sum() / len(df)) * 100
        return null_percentage

   def plot_nulls(df):
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
        plt.title("Missing Values in DataFrame")
        plt.show()

   def columns_with_nulls(df):
       null_columns = df.columns[df.isnull().any()]
       return null_columns


   def nulls_above_50_percent(df):
       null_percentage = (df.isnull().sum() / len(df)) * 100
       columns_above_threshold = null_percentage[null_percentage > 50].index
       if not columns_above_threshold.empty:
         print(f"Columns with more than 50% null values: {columns_above_threshold}")
       else:
         print("No columns have more than 50% null values.")