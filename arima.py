from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Petrol price in $/bbl'):
    plt.figure(figsize=(16,5))
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

# 1,1,2 ARIMA Model
df = pd.read_csv('fuel_price_data.csv', names=['value'], header=0)
model = ARIMA(df.value, order=(1,1,2))
model_fit = model.fit(disp=0)
print(model_fit.summary())
model_fit.plot_predict(dynamic=False)
plot_df(df, x=df.index, y=df.value, title='Monthly petrol price value in India from 2000 to 2020')