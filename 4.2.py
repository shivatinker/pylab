import pandas as pd
from datetime import datetime

data = pd.read_excel('filter2.xlsx', sheet_name='filter2', parse_dates=['Shelf_life'])
data['Discount'] = datetime.utcnow() - data['Shelf_life'] >= pd.to_timedelta(3, unit='d')
print(data)
print('\n')
print(data[data.Discount == True])
print('\n')
print(data[(data.Discount == True) & (data.CountryOfOrigin == 'Belarus')])
print('\n')
print(data[(data.Discount == False) & (data.Product == 'Milk "Good health"')])
print('\n')
print(data[(data.Discount == False) & (data.CountryOfOrigin == 'Ukraine')])
print('\n')
print(data[(data.Discount == True) & (data.Quantity > 20)])
print('\n')
print(data[((data.CountryOfOrigin == 'Belarus') & (data.Quantity > 30)) | (
        (data.CountryOfOrigin == 'Ukraine') & (data.Discount == True))])
print('\n')
print(
    data[((data.CountryOfOrigin == 'Belarus') & (data.Price < 20)) | ((data.Quantity < 40) & (data.Discount == True))])
