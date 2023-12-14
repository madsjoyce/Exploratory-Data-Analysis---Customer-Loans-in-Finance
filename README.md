# <ins> EXPLORATORY DATA ANALYSIS - CUSTOMER LOANS IN FINANCE

![Finance Gif](<iframe src="https://giphy.com/embed/NyniJ2Nf2ZzlE8GYsl" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/JustStartInvesting-NyniJ2Nf2ZzlE8GYsl">via GIPHY</a></p>)

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

**Step 4.** Run the db_utilis.py file to load the loan_payments.data file.
- Enter the folowing command into your terminal: ```python db_utilis.py```
- Verify that the 'loan_payments_data.csv' file has loaded into your 'exploratory_data_analysis' directory on your local machine.

**Step 5.** Ready for Analysis.
- With the data successfully loaded, you are now ready to read and analyse it for your exploratory data analysis tasks.

### 3. Usage Instructions
This project's intended use is to load loan payment data onto your local machine so that you can perform exploratory data analysis. 

### 4. File Structure of the Project
- **credentials.yaml** - This file includes all the credentials needed to load the dataframe from AWS RDS.
- **.gitignor** - This is a security measure. It includes the 'credentials.yaml' file and will stop these private credentials being pushed to GitHub.
- **db_utilis.py** - This contains the code needed to fetch and load the data from AWS RDS.
- **load_payments_data.csv** - This conains all the markdown information needed to run this project.

### 5. License Information
Please click on the link below for license information:

[Link for License](LICENSE.txt)