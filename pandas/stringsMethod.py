#print('rifai Kuci'.upper()) # Buyuk harflere donustur

import pandas as pd

orders = pd.read_table('orders.tsv')
# print(orders.head())
#print(orders.columns)

#orders.item_name = orders.item_name.str.upper() # buyuk harfler

# print(orders.item_name)
# print(orders.item_name.str.contains("Chicken".upper()))
orders.item_price = orders.item_price.str.replace('$',' ')

print(orders.item_price)