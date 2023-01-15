import pandas as pd
import glob

# Create list to store multiple filepaths
filepaths = glob.glob('invoices/*.xlsx') # Get everythong with ending xlsx
print(filepaths)

# Read all files
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    print(df)