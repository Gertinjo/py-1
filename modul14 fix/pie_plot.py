import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('avgIQpercountry.csv')



nobel_prize_by_continent = df.groupby('Continent')['Nobel Prices'].sum()

no_of_continents = nobel_prize_by_continent.count()

print(no_of_continents)

colors = ['skyblue', 'gold' , 'red' , 'blue' , 'lime' , 'green' , 'orange' , 'purple']

plt.figure(figsize=(10, 10))

nobel_prize_by_continent.plot(kind='pie', colors=colors , autopct='%1.1f%%')

plt.title('Distribution of Nobel Prizes by continent')

plt.axis('equal')

plt.ylabel('')
plt.tight_layout()

plt.show()