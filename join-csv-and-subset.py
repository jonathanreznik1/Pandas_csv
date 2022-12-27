import pandas as pd
import csv

# Make sure to python install -r requirements.txt

# Insert path to file
CSV_File1 = 'LA City Council District 5 EMAIL List.xlsx - Sheet1.csv'
CSV_File2 = 'LACCD 2022 Voter History - NG18NG20.xlsx - Sheet1.csv'

# Specify field to join 
join_col = 'voter_id'

# Specify filters for data fields and values
field1 = '11/03/2020 4193'
value1 = 'N'
field2 ='11/06/2018 3861'
value2 = 'N'

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
