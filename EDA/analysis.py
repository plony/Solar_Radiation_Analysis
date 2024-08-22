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
#evaluate impact of Cleaning
avg_sensor_readings = data.groupby('Cleaning')[['ModA' , 'ModB']].mean()
print(avg_sensor_readings)
#Correlation Analysis
correlation_matrix + data[['GHI', 'DNI', 'DHI', 'TModA','TModB','WS','WSgust','WD']].corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()
#temperature analysis
plt.scatter(data['RH'], data['Tamb'])
plt.xlabel('relative humidity')
plt.title('temperature vs Relative humidity')
plt.show()
#Histogram