# <ins> EXPLORATORY DATA ANALYSIS - CUSTOMER LOANS IN FINANCE
![Finance_picture](Finance.jpeg)
## Table of Contents 
1. Description of the Project
2. Installation Instructions
3. Usage Instructions
4. File Structure of the Project
5. License Information


### 1. What is the aim of this Project?
The aim of this project is to develop my skills in exploratory data analysis on the loan_payments_data database, by immersing myself in the fictitious role of being a large financial institution's employee. Through this project I have learned that managing loans is a critical component of business operations.

By gaining a comprehensive understanding of the loan portfolio data, I have been able to ensure that informed decisions are made about loan approvals and risk is efficiently managed.

Through EDA on the loan portfolio, using various statistical and data visualisation techniques I have been able to uncover patterns, relationships, and anomalies in the loan data.

The information created through my EDA will enable the business to make more informed decisions about loan approvals, pricing, and risk management.

By conducting EDA on the loan data, I have gained a deeper understanding of the risk and return associated with the business' loans, and I have also been able to improve the performance and profitability of the loan portfolio.


### 2. Installation Instructions
To install:

**Step 1.** Clone the repository to your machine.
- Clone the repository to your machine by entering the following command in your terminal:
: ```git clone https://github.com/madsjoyce/Exploratory-Data-Analysis--Customer-Loans-in-Finance.git```.

 **Step 2.** Navigate to the project directory.
     - Navigate to the project directory by entering the following command into your terminal: ```cd exploratory_data_analysis```.

**Step 3.** Ensure you have the correct packages installed to your local machine:
- Install Python PyYAML Package by entering the following command into your terminal: ```pip install PyYAML```
- Install Python Pandas Package by entering the following command into your terminal:```pip install pandas```
- Install Python Numpy Package by entering the following command into your terminal:```pip install numpy```
- Install Python Matplotliib Package by entering the following command into your terminal:```pip install matplotlib```
- Install Python Seaborn Package by entering the following command into your terminal:```pip install seaborn```

**Step 4.** Create a credentials.yaml file to store your database credentials.
- If using GitHub, remember to add this file to your .gitignore file in your repository, as you don't want your credentials being pushed to GitHub for security reasons.
- You will need the following credentials in the .yaml file: RDS_HOST, RDS_PASSWORD, RDS_USER, RDS_DATABASE, RDS_PORT.

**Step 5.** Execute all .py files in the following order to ensure all classes are ready to run for analysis.
1. db_utilis.py
2. DataTransform.py
3. DataFrameInfo.py
4. Plotter.py
5. DataFrameTransform.py 

**Step 6.** Ready for Analysis.
- With the classes successfully loaded, you can now go through the .py files' corresponding notebook, in the same order, and execute the code cells to start to transform and visualise the data. 
- Please note, that you will need to run the top boxes in both Milestone_3 and Milestone_4 notebooks to ensure that the database is correctly transformed and ready for analysis.

### 3. Usage Instructions
This project's intended use is to load loan payment data onto your local machine so that you can perform exploratory data analysis. 

### 4. File Structure of the Project
- **credentials.yaml** - This file includes all the credentials needed to load the dataframe from AWS RDS.
- **.gitignor** - This is a security measure. It includes the 'credentials.yaml' file and will stop these private credentials being pushed to GitHub.
- **LICENCE.txt** - This contains the licensing information for this repository.
- **Finance.jpeg** - This contains an image I have used in this README.md file.
- **db_utilis.py** - This contains the code needed to fetch and load the data from AWS RDS, by creating the RDSDatabaseConnector class.
- **loan_payments_data.csv** - This conains all the markdown information needed to run this project.
- **DataTransform.py** - This contains the DataTransform class that can transform the loan_payment_data dataframe columns' to have suitable datatypes.
- **DataTransform.ipynb** - This notebook contains the code to test the DataTransform class on the loan_payments_data dataframe and create the transformed_df.csv file.
- **DataFrameInfo.py** - This file contains the class DataDrameInfo. Its code helps to describe null values and unique values within the dataframe.
- **DataFrameInfo.ipynb** - This notebook contains code that uses the DataFrameInfo class to find out various information regarding the dataframe.
- **Plotter.py** - This python file contains the class Plotter, which has useful code to help plot and visualise information about the dataframe.
- **DataFrameTransform.py** - This contains the class DataFrameTransform which contains the code to drop columns, impute columns, remove outliers and remove highly correlated columns.
- **Milestone_3.ipynb** - Contains the code that performs EDA on the dataframe using both the Plotter and the DataFrameTransform classes.
- **Milestone_4.ipynb** - Contains the code using all other classes to analyse and visualise both historical and future aspects of the transformed_df. 

### 5. License Information
Please click on the link below for license information:

[Link for License](LICENSE.txt)