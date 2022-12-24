import csv
import pandas as pd

# Make sure to have pandas installed by running in the project folder
# python install -r requirements.txt

# Pandas can open and read in files
df1 = pd.read_csv('filename1')  # Replace with actual path of the Email List
df2 = pd.read_csv('filename2')       # Replace with the Nonvoter list

# A join of both files based on the column
df3 = df1.join(df2.set_index('voter_id'), on='voter_id')

# Subset the data and write to two new files
out1 = df3[(df3['11/03/2020 4193'] == 'N') | (df3['11/06/2018 3861'] == 'N')]
out1.to_csv('newfile1.csv')
# type: ignore
out2 = df3[(df3['11/03/2020 4193'] != 'N') | (df3['11/06/2018 3861'] != 'N')]
out2.to_csv('newfile2.csv')
