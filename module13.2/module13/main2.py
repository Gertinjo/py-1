import pandas as pd


product = ['Apple ', 'Banana' , 'Orange']

sales = [150 , 200 , 300]


sales_series = pd.Series(sales , index=product)

print(sales_series)