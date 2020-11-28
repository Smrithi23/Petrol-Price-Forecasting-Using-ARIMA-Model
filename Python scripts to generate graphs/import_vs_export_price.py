import matplotlib.pyplot as plt

products_imported_data = {'2011-2012': 68091, '2012-13': 68852, '2013-14': 75896, '2014-15': 74644, '2015-16': 65361, '2016-17': 71566, '2017-18': 88374, '2018-19': 113665, '2019-20': 125742}
oil_import_data = {'2011-2012': 672220, '2012-13': 784652, '2013-14': 864875, '2014-15': 687416, '2015-16': 416579, '2016-17': 470159, '2017-18': 566450, '2018-19': 783183, '2019-20': 717001}
total_import_data = {'2011-2012': 740311, '2012-13': 853504, '2013-14': 940771, '2014-15': 762060, '2015-16': 481940, '2016-17': 541725, '2017-18': 654824, '2018-19': 896848, '2019-20': 842743}
products_exported_data = {'2011-2012': 284644, '2012-13': 320090, '2013-14': 368279, '2014-15': 288580, '2015-16': 176780, '2016-17': 194893, '2017-18': 225388, '2018-19': 267697, '2019-20': 254018}
net_import_data = {'2011-2012': 45566, '2012-13': 533415, '2013-14': 572492, '2014-15': 473481, '2015-16': 305160, '2016-17': 346832, '2017-18': 429436, '2018-19': 629152, '2019-20': 588725}

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


fig.suptitle("Import vs Export of Petroleum Products")
plt.xlabel("Years")
plt.ylabel("Petroleum Product in Crores")
plt.legend()
plt.show()