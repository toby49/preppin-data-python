#This challenge uses the solution from the Week 1 output, so first import along with pandas
import pandas as pd
from PD_2024_Wk1_Solution import df_flow_card_holders, df_non_flow_card_holders

#Union the two data frames together => pd.concat([df1, df2], axis=0)
df = pd.concat([df_non_flow_card_holders, df_flow_card_holders], axis=0)

#Parse quarter from the Date column
df['Quarter'] = df['Date'].dt.quarter

#Pivot data and create separate dfs for each type of aggregation => df.pivot_table(index,columns,values,aggfunc)
#Median Price by Quarter, Flow Card? and Class
df_med = df.pivot_table(
    index=['Quarter', 'Flow Card?'],
    columns='Class',
    values='Price',
    aggfunc='median'
)
df_med['Aggregation'] = 'Median' #Add hard-coded column

#Minimum Price by Quarter, Flow Card? and Class
df_min = df.pivot_table(
    index=['Quarter', 'Flow Card?'],
    columns='Class',
    values='Price',
    aggfunc='min'
)
df_min['Aggregation'] = 'Minimum' #Add hard-coded column

#Maximum Price by Quarter, Flow Card? and Class
df_max = df.pivot_table(
    index=['Quarter', 'Flow Card?'],
    columns='Class',
    values='Price',
    aggfunc='max'
)
df_max['Aggregation'] = 'Maximum' #Add hard-coded column

#Union aggregated data flows together
df_agg = pd.concat([df_max, df_min, df_med], axis=0)

#Rename columns to correct data quality issues - at this point Economy is the most expensive!
df_agg = df_agg.rename(columns={
                    'First Class': 'Economy',
                    'Business Class': 'Premium',
                    'Premium Economy': 'Business',
                    'Economy': 'First'}) #Use df.rename(columns={}) to only rename specified columns. df.colums = ['Column1', 'Column2'...] requires you to list all columns

#Print Output
print(df_agg)

