import pandas as pd


#Step 1: Main Branch

#Read excel package
#requires openpyxl package
data = pd.read_excel("store_inventory.xlsx", sheet_name=None)

#Generate Sheet Summary Statistics
for (key, value) in data.items():
    print(f"store-{key}: {value.shape[0]} rows x {value.shape[1]} columns")
    columns = []
    for col in value.columns:
        columns.append(col)
    print(f"store-{key}: {columns}")

#Feature 1: Branch 1
#TODO Create Calculated Values

#Feature 2: Branch 2
#TODO Create summary statistics by group

#Step 2: Main Branch
#Sheet Summary Statistics with Calculated Values

#Feature 3: Branch 3
#TODO Combine datasets
