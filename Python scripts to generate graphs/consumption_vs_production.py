import matplotlib.pyplot as plt

products_consumed_data = {'2011': 148132, '2012': 157057, '2013': 158407, '2014': 165520, '2015': 184674, '2016': 194597, '2017': 206166, '2018': 213216, '2019': 214127}
products_produced_data = {'2011': 204453, '2012': 218248, '2013': 220740, '2014': 221077, '2015': 231866, '2016': 243515, '2017': 254289, '2018': 262356, '2019': 262940}

products_consumed_names = list(products_consumed_data.keys())
products_consumed_values = list(products_consumed_data.values())

products_produced_names = list(products_produced_data.keys())
products_produced_values = list(products_produced_data.values())

fig, ax = plt.subplots()
ax.plot(products_consumed_names, products_consumed_values, label="Consumption")
ax.plot(products_produced_names, products_produced_values, label="Production")

fig.suptitle("Production vs Consumption of Petroleum Products")
plt.xlabel("Years")
plt.ylabel("Petroleum Product in Metric Tonnes")
plt.legend()
plt.show()