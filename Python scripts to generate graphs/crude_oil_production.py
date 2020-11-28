import matplotlib.pyplot as plt

crude_oil_data = {'2011-2012': 35.9, '2012-13': 35.7, '2013-14': 35.9, '2014-15': 35.9, '2015-16': 35.5, '2016-17': 34.5, '2017-18': 34.0, '2018-19': 32.5, '2019-20': 30.5}
condensate_data = {'2011-2012': 2.2, '2012-13': 2.2, '2013-14': 1.9, '2014-15': 1.6, '2015-16': 1.4, '2016-17': 1.5, '2017-18': 1.6, '2018-19': 1.7, '2019-20': 1.6}
total_data = {'2011-2012': 38.1, '2012-13': 37.9, '2013-14': 37.8, '2014-15': 37.5, '2015-16': 36.9, '2016-17': 36.9, '2017-18': 35.7, '2018-19': 34.2, '2019-20': 32.2}

crude_oil_names = list(crude_oil_data.keys())
crude_oil_values = list(crude_oil_data.values())

condensate_names = list(condensate_data.keys())
condensate_values = list(condensate_data.values())

total_names = list(total_data.keys())
total_values = list(total_data.values())

fig, ax = plt.subplots()
ax.plot(crude_oil_names, crude_oil_values, label = "Crude Oil")
ax.plot(condensate_names, condensate_values, label = "Condensate")
ax.plot(total_names, total_values, label="Total")

fig.suptitle("Indigenous Crude Oil Production in Million Metric Tonnes")
plt.xlabel("Years")
plt.ylabel("Crude Oil Production")
plt.legend()
plt.show()