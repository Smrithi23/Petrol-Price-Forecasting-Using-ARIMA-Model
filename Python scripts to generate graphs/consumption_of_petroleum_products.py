import matplotlib.pyplot as plt

products_data = {'2011-2012': 148132, '2012-13': 157057, '2013-14': 158407, '2014-15': 165520, '2015-16': 184674, '2016-17': 194597, '2017-18': 206166, '2018-19': 213216, '2019-20': 214127}

products_names = list(products_data.keys())
products_values = list(products_data.values())

fig, ax = plt.subplots()
ax.plot(products_names, products_values)

fig.suptitle("Consumption of Petroleum Products in '000 Metric Tonne")
plt.xlabel("Years")
plt.ylabel("Petroleum Product Consumption")
plt.show()