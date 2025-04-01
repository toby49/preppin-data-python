import pandas as pd

#Define Starter CSV filepath 
csv = "Inputs\PD 2024 Wk 1 Input.csv"

#Load CSV into DataFrame
df = pd.read_csv(csv)

#Split Flight Details field. expand=True is splits into separate columns as opposed to a list in the Flight Details field
df_split = df['Flight Details'].str.split('//', expand=True)

#Rename split columns
df_split.columns = ['Date', 'Flight Number', 'Route', 'Class', 'Price']

#Split 'Route' column
df_split[['From', 'To']] = df_split['Route'].str.split('-', expand=True)

#Drop the original "Route" column if no longer needed
df_split.drop(columns=['Route'], inplace=True)

#Change field data types => note: use df['fieldX'] to overwrite a column within the dataframe. Call df to overwrite the entire df
df_split['Date'] = pd.to_datetime(df_split['Date'], format='%Y-%m-%d', errors='coerce') #errors='coerce' returns null values for any invalid rows instead of retuning error
df_split['Price'] = pd.to_numeric(df_split['Price'], errors='coerce')

#Merge df_split back to original df, excluding the flight details column 
df_stage = pd.concat([df_split, df.drop(columns=['Flight Details'])],  axis=1) #concat([df1, df2], axis=1) joins two dfs side by side. axis=1 unions

#Replace flow card values of 1/0 to Yes/No
df_stage['Flow Card?'] = df_stage['Flow Card?'].replace({1: 'Yes', 0: 'No'})

#Create DataFrame for Flow Card holders (Flow Card == 'Yes')
df_flow_card_holders = df_stage[df_stage['Flow Card?'] == 'Yes']

#Create DataFrame for non-Flow Card holders (Flow Card == 'No')
df_non_flow_card_holders = df_stage[df_stage['Flow Card?'] == 'No']

#Display output
print("Flow Card Holders:")
print(df_flow_card_holders)

print("Non-Flow Card Holders:")
print(df_non_flow_card_holders)
