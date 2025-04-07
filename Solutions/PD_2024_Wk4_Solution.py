import pandas as pd

#Define excel input file path
xlsx = 'Inputs\PD 2024 Wk 4 Input.xlsx'

#Create df for flow_card Customers
df_flow_card = pd.read_excel(xlsx, sheet_name='Flow Card')
df_flow_card['Flow_card?'] = 'Y' #Add Y/N field for whether they hold a Flow Card

#Create df for non Flow card Customers
sheets=['Non_flow Card','Non_flow Card2']
df_dict = pd.read_excel(xlsx, sheet_name=sheets) #This returns a dictionary when reading a list of sheets at once
df_non_flow_card = pd.concat(df_dict.values(), ignore_index=True) #Use values() to return only the dfs, ie not the sheetnames (dictionary)
df_non_flow_card['Flow_card?'] = 'N' #Add Y/N field for whether they hold a Flow Card

#Union dfs 
df = pd.concat([df_flow_card, df_non_flow_card], ignore_index=True)

#Count the number of bookings for each Class, Row and Seat
df_bookings = df.groupby(['Class', 'Row', 'Seat']).size().reset_index(name='Bookings')

#Read in seat plan sheet from input file
df_seats = pd.read_excel(xlsx, sheet_name='Seat Plan')

#Right Join the bookings and sheets dfs
df_joined = pd.merge(df_bookings, df_seats, how='right' , on=['Class', 'Row', 'Seat'], indicator=True)

#Filter df to return only available seats
df_available = df_joined[df_joined['_merge'] == 'right_only']

#Clean df to match challenge output
df_available = df_available[['Class', 'Row', 'Seat']].reset_index(drop=True) #.reset_index(drop=True) to exclude index column when resetting

#Print solution 
print(df_available)

