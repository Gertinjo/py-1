import pandas as pd

data = {'Name': ['Gerti' , 'Dreni' , 'Deon' , 'Trimi'],
        'Age': [12, 16 , 15 , 13],
        'City': ['Prishtina' ,'Prishtina' ,'Prishtina' ,'Prishtina' , ]}

df = pd.DataFrame(data)

print(df)