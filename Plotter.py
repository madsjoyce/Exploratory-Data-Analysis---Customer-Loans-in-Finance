import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:

   def plot_nulls(df):
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
        plt.title("Missing Values in DataFrame")
        plt.show()


  
