import pandas as pd
import csv

# Make sure to python install -r requirements.txt

# Insert path to file
CSV_File1 = '{filename1}.csv'
CSV_File2 = '{filename2}.csv'

# Specify field to join 
join_col = '{col_name}'

# Specify filters for data fields and values
field1 = '{field1}'
value1 = '{val1}'
field2 ='{field2}'
value2 = '{val2}'

# Pandas
df1 = pd.read_csv(CSV_File1)
df2 = pd.read_csv(CSV_File2)
df3 = df1.join(df2.set_index(join_col), on=join_col)    #join files

# Subset data
out1 = df3[(df3[field1] == value1) | (df3[field2] == value2)]
out2 = df3[(df3[field1] != value1) | (df3[field2] != value2)]

# Write file output
out1.to_csv('newfile1.csv')
out2.to_csv('newfile2.csv')
