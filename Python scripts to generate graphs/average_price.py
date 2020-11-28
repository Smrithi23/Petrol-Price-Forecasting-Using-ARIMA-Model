import matplotlib.pyplot as plt

avg_price_data = {'2011-2012': 111.89, '2012-13': 107.97, '2013-14': 105.52, '2014-15': 84.16, '2015-16': 46.17, '2016-17': 47.56, '2017-18': 56.43, '2018-19': 69.88, '2019-20': 60.47}

avg_price_names = list(avg_price_data.keys())
avg_price_values = list(avg_price_data.values())

fig, ax = plt.subplots()
ax.plot(avg_price_names, avg_price_values)
plt.suptitle("Average Price of Crude Oil in $/bbl")
plt.xlabel("Years")
plt.ylabel("Average Price in $/bbl")
plt.show()