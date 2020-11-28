import matplotlib.pyplot as plt

products_imported_data = {'2011-2012': 15849, '2012-13': 16354, '2013-14': 16697, '2014-15': 21301, '2015-16': 29456, '2016-17': 36287, '2017-18': 35461, '2018-19': 33348, '2019-20': 43788}
oil_import_data = {'2011-2012': 171729, '2012-13': 184795, '2013-14': 189238, '2014-15': 189435, '2015-16': 202850, '2016-17': 213932, '2017-18': 220433, '2018-19': 226498, '2019-20': 226955}
total_import_data = {'2011-2012': 187579, '2012-13': 201149, '2013-14': 205935, '2014-15': 210736, '2015-16': 232306, '2016-17': 250219, '2017-18': 255894, '2018-19': 259846, '2019-20': 270742}
products_exported_data = {'2011-2012': 60837, '2012-13': 63408, '2013-14': 67864, '2014-15': 63932, '2015-16': 60539, '2016-17': 65513, '2017-18': 66833, '2018-19': 61096, '2019-20': 65685}
net_import_data = {'2011-2012': 126741, '2012-13': 137742, '2013-14': 138071, '2014-15': 146804, '2015-16': 171768, '2016-17': 184706, '2017-18': 189061, '2018-19': 198750, '2019-20': 205057}

products_imported_names = list(products_imported_data.keys())
products_imported_values = list(products_imported_data.values())

oil_import_names = list(oil_import_data.keys())
oil_import_values = list(oil_import_data.values())

total_import_names = list(total_import_data.keys())
total_import_values = list(total_import_data.values())

products_exported_names = list(products_exported_data.keys())
products_exported_values = list(products_exported_data.values())

net_import_names = list(net_import_data.keys())
net_import_values = list(net_import_data.values())

fig, ax = plt.subplots()
ax.plot(products_imported_names, products_imported_values, label="Products Imported")
ax.plot(oil_import_names, oil_import_values, label="Oil Imported")
ax.plot(total_import_names, total_import_values, label="Total Imported")
ax.plot(products_exported_names, products_exported_values, label="Products Exported")
ax.plot(net_import_names, net_import_values, label="Net Import")


fig.suptitle("Import vs Export of Petroleum Products in '000 Metric Tonnes")
plt.xlabel("Years")
plt.ylabel("Petroleum Product in '000 Metric Tonnes")
plt.legend()
plt.show()