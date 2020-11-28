import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
# Import Data
df = pd.read_csv('fuel_price_data.csv')

# Draw Plot
fig, (ax1) = plt.subplots(1)
plot_pacf(df.value.tolist(), ax=ax1, lags=20)


# font size of tick labels
ax1.tick_params(axis='both', labelsize=12)
plt.show()