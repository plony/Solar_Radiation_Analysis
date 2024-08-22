import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
data = pd.read_csv('benin-malanville.csv')
print(data.describe())
print(data.isnull().sum())
print(data[data['GHI']<0].count())
# Time Series Anysis
plt.plot(data['GHI'])
plt.xlabel('Time')
plt.ylabel('GHI')
plt.title('GHI over Time')
plt.show()