import pandas as pd

data_path = r'../../data/landscape_36x11.xlsx'
label_path = r'../../data/landscape_36x11_category.xlsx'

data = pd.read_excel(data_path)
label_data = pd.read_excel(label_path)
label_data = label_data[['id', 'category']]
print(data)
new_data = pd.merge(data, label_data, on=['id'])
print(new_data)
new_data.to_excel(r'../../data/landscape_36x11_category.xlsx')
