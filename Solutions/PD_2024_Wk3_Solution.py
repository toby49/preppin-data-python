#Import pandas and dataframes from week 1 solution 
import pandas as pd
from PD_2024_Wk1_Solution import df_flow_card_holders, df_non_flow_card_holders

#Define excel input file path
xlsx = 'Inputs\PD 2024 Wk 3 Input.xlsx'

#Read all sheet names
sheet_names = pd.ExcelFile(xlsx).sheet_names

#Read each sheet into a dataframe and store in a list 
dfs = [pd.read_excel(xlsx, sheet_name=sheet) for sheet in sheet_names]

#Union all dataframes
df_targets = pd.concat(dfs, ignore_index=True) #Union excel sheets
df_sales = pd.concat([df_flow_card_holders, df_non_flow_card_holders], ignore_index=True)

#Correct the Classes being incorrect as per the solution from last week, whilst abbreviating so that we can join with targets dataframe
df_sales['Class'] = df_sales['Class'].replace({
    'Economy': 'FC',
    'First Class': 'E',
    'Business Class': 'PE',
    'Premium Economy': 'BC'
})

#Parse month from date column in sales df
df_sales['Month'] = df_sales['Date'].dt.month

#Aggregate monthly sales by class
df_monthly_sales = df_sales.groupby(['Month', 'Class'])['Price'].sum()

#Join sales and targets dataframes
df_merged = pd.merge(df_monthly_sales,df_targets, on=['Month','Class'])

#Calculate Difference to Target Column
df_merged['Difference to Target'] = df_merged['Price'] - df_merged['Target'] 

#Print solution
print(df_merged)