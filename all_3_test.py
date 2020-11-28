import pmdarima
from pmdarima.arima.utils import ndiffs
import pandas as pd
df = pd.read_csv('fuel_price_data.csv', names=['value'], header=0)
y = df.value

## Adf Test
n1 = ndiffs(y, test='adf')  # 2

# KPSS test
n2 = ndiffs(y, test='kpss')  # 0

# PP test:
n3 = ndiffs(y, test='pp')  # 2

print(n1, n2, n3)