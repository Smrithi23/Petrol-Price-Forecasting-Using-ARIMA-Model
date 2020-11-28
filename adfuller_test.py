from statsmodels.tsa.stattools import adfuller
from numpy import log
import pandas as pd
df = pd.read_csv('fuel_price_data.csv', names=['value'], header=0)
result = adfuller(df.value.dropna())
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])