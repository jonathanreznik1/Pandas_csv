import pandas as pd
import csv

# Make sure to have pandas installed by running in the project folder
# python install -r requirements.txt
CSV_File1 = 'LA City Council District 5 EMAIL List.xlsx - Sheet1.csv'
CSV_File2 = 'LACCD 2022 Voter History - NG18NG20.xlsx - Sheet1.csv'

# Specify the field to join 
join_col = 'voter_id'

# Filters for subsetting data
field1 = '11/03/2020 4193'
value1 = 'N'
field2 ='11/06/2018 3861'
value2 = 'N'

# Pandas can open and read in files
df1 = pd.read_csv(CSV_File1)  # Replace with actual path of the Email List
df2 = pd.read_csv(CSV_File2)       # Replace with the Nonvoter list

# A join of both files based on the column
df3 = df1.join(df2.set_index(join_col), on=join_col)

# Subset the data and write to two new files
out1 = df3[(df3[field1] == value1) | (df3[field2] == value2)]
out1.to_csv('newfile1.csv')

# type: ignore
out2 = df3[(df3[field1] != value1) | (df3[field2] != value2)]
#out2 = df3[(df3['11/03/2020 4193'] != 'N') | (df3['11/06/2018 3861'] != 'N')]
out2.to_csv('newfile2.csv')
