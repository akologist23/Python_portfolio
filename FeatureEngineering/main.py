import pandas as pd


#Step 1: Main Branch

#Read excel package
#requires openpyxl package
data = pd.read_excel("store_inventory.xlsx", sheet_name=None)

#Generate Sheet Summary Statistics
# for (key, value) in data.items():
#     print(f"store-{key}: {value.shape[0]} rows x {value.shape[1]} columns")
#     columns = []
#     for col in value.columns:
#         columns.append(col)
#     print(f"store-{key}: {columns}")

#Feature 1: Branch 1
#TODO Create Calculated Values
for (store, df) in data.items():
    df['total_value'] = df['qty_stock'] * df['unit price']
    #print(df)

#Feature 2: Branch 2
#TODO Create summary statistics by group
item_dict = {}
for (store, df) in data.items():
    #print(df.groupby(by='category').size())
    output = df.groupby(by='category')['qty_stock'].agg(['count','sum'])
    #print(output)
    for item in output.index:
        count = output[output.index == item]['count'].values[0].item()
        sum = output[output.index == item]['count'].values[0].item()
        item_dict[item] = {'count':  count,
                            'sum': sum
                           }

print(item_dict)

#Step 2: Main Branch
#Sheet Summary Statistics with Calculated Values
# for (store, df) in data.items():
#     print(f"store-{store}: total inventory value ${df['total_value'].sum()}")
#     print(df.describe())

#Feature 3: Branch 3
#TODO Combine datasets
