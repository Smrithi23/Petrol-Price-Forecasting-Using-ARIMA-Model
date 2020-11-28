import matplotlib.pyplot as plt

products_data = {'2011-2012': 204453, '2012-13': 218248, '2013-14': 220740, '2014-15': 221077, '2015-16': 231866, '2016-17': 243515, '2017-18': 254289, '2018-19': 262356, '2019-20': 262940}

products_names = list(products_data.keys())
products_values = list(products_data.values())

fig, ax = plt.subplots()
ax.plot(products_names, products_values)

fig.suptitle("Production of Petroleum Products in '000 Metric Tonne")
plt.xlabel("Years")
plt.ylabel("Petroleum Product Production")
plt.show()