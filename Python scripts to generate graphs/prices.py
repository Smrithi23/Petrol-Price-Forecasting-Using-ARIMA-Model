import matplotlib.pyplot as plt

data_2011 = {'April': 118.64, 'May': 110.80, 'June': 109.99, 'July': 112.53, 'Aug': 106.94, 'Sept': 108.79, 'Oct': 106.11, 'Nov': 109.62, 'Dec': 107.19, 'Jan': 110.47, 'Feb': 117.67, 'March': 123.61}
data_2012 = {'April': 117.97, 'May': 108.05, 'June': 94.51, 'July': 100.34, 'Aug': 110.07, 'Sept': 111.77, 'Oct': 109.79, 'Nov': 107.87, 'Dec': 107.28, 'Jan': 109.55, 'Feb': 112.68, 'March': 106.45}
data_2013 = {'April': 101.57, 'May': 101.10, 'June': 101.11, 'July': 104.86, 'Aug': 108.45, 'Sept': 109.47, 'Oct': 107.37, 'Nov': 106.55, 'Dec': 108.72, 'Jan': 105.29, 'Feb': 106.19, 'March': 105.30}
data_2014 = {'April': 105.56, 'May': 106.85, 'June': 109.05, 'July': 106.30, 'Aug': 101.89, 'Sept': 96.96, 'Oct': 86.83, 'Nov': 77.58, 'Dec': 61.21, 'Jan': 46.59, 'Feb': 56.43, 'March': 55.18}
data_2015 = {'April': 59.07, 'May': 63.82, 'June': 61.75, 'July': 56.30, 'Aug': 47.33, 'Sept': 46.10, 'Oct': 46.68, 'Nov': 42.50, 'Dec': 35.68, 'Jan': 28.08, 'Feb': 30.53, 'March': 36.42}
data_2016 = {'April': 39.88, 'May': 45.01, 'June': 46.96, 'July': 43.52, 'Aug': 44.38, 'Sept': 44.48, 'Oct': 49.25, 'Nov': 44.46, 'Dec': 52.74, 'Jan': 54.08, 'Feb': 54.86, 'March': 51.47}
data_2017 = {'April': 52.49, 'May': 50.57, 'June': 46.56, 'July': 47.86, 'Aug': 50.63, 'Sept': 54.52, 'Oct': 56.06, 'Nov': 61.32, 'Dec': 62.29, 'Jan': 67.06, 'Feb': 63.54, 'March': 63.80}
data_2018 = {'April': 69.22, 'May': 75.25, 'June': 73.83, 'July': 73.47, 'Aug': 72.53, 'Sept': 77.88, 'Oct': 80.08, 'Nov': 65.40, 'Dec': 57.77, 'Jan': 59.27, 'Feb': 64.53, 'March': 66.74}
data_2019 = {'April': 71.00, 'May': 70.01, 'June': 62.37, 'July': 63.63, 'Aug': 59.35, 'Sept': 61.72, 'Oct': 59.70, 'Nov': 62.53, 'Dec': 65.50, 'Jan': 64.31, 'Feb': 54.63, 'March': 33.36}

data_2011_names = list(data_2011.keys())
data_2011_values = list(data_2011.values())

data_2012_names = list(data_2012.keys())
data_2012_values = list(data_2012.values())

data_2013_names = list(data_2013.keys())
data_2013_values = list(data_2013.values())

data_2014_names = list(data_2014.keys())
data_2014_values = list(data_2014.values())

data_2015_names = list(data_2015.keys())
data_2015_values = list(data_2015.values())

data_2016_names = list(data_2016.keys())
data_2016_values = list(data_2016.values())

data_2017_names = list(data_2017.keys())
data_2017_values = list(data_2017.values())

data_2018_names = list(data_2018.keys())
data_2018_values = list(data_2018.values())

data_2019_names = list(data_2019.keys())
data_2019_values = list(data_2019.values())

fig, ax = plt.subplots()
ax.plot(data_2011_names, data_2011_values, label="2011-12")
ax.plot(data_2012_names, data_2012_values, label="2012-13")
ax.plot(data_2013_names, data_2013_values, label="2013-14")
ax.plot(data_2014_names, data_2014_values, label="2014-15")
ax.plot(data_2015_names, data_2015_values, label="2015-16")
ax.plot(data_2016_names, data_2016_values, label="2016-17")
ax.plot(data_2017_names, data_2017_values, label="2017-18")
ax.plot(data_2018_names, data_2018_values, label="2018-19")
ax.plot(data_2019_names, data_2019_values, label="2019-20")

fig.suptitle("Petrol Price in $/bbl")
plt.xlabel("Years")
plt.ylabel("Petrol Price in $/bbl")
plt.legend()
plt.show()