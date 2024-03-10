import pandas as pd
from faker import Faker
import random

col_ram = []
col_name = []
col_price = []
col_hasDualSim = []

fake = Faker()

existing_brands = ['Apple', 'Samsung', 'Huawei', 'Xiaomi',
                   'Oppo', 'Vivo', 'OnePlus', 'Google', 'Sony', 'LG']



# Fill the empty lists with data
random.seed(10)
for i in range(1, 1001):
    col_ram.append(random.randint(2, 12))
    col_name.append(random.choice(existing_brands))
    col_price.append(round(fake.random_number(
        digits=4, fix_len=True) / 100, 2))
    col_hasDualSim.append(fake.boolean())

# Create a data frame from the lists
df = pd.DataFrame.from_dict({'Brand': col_name,
                             'RAM': col_ram,
                             'Price': col_price,
                             'Has Dual Sim': col_hasDualSim})

# Convert the data types of the columns
df['Brand'] = pd.Series(['Brand'], dtype="string")

# explore data types
print(df.dtypes)

################################################################################

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('smartphone_data.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object
df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

# Get the xlsxwriter objects from the dataframe writer object
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Get the dimensions of the dataframe
(max_row, max_col) = df.shape

# Create a list of column headers, to use in add_table()
column_settings = [{'header': column} for column in df.columns]

# Add the Excel table structure. Pandas will add the data
worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

# Make the columns wider for clarity
worksheet.set_column(0, max_col - 1, 20)


# Close the Pandas Excel writer and output the Excel file  
writer.close()
################################################################################