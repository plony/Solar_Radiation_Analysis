import pandas as pd
import numpy as np
import os, sys
#os.getcwd()
#sys.path.insert(0, os.path.abspath('../'))
#from script.plot_correlation_heatmap
import matplotlib.pyplot as plt
import seaborn as sns
#load the Dataset
data = pd.read_csv('K:\data analysis\Solar_Radiation_Analysis\Data\sierraleone-bumbuna.csv')
#summary statistics
print(data.describe())
#Data Quality Check
print(data.isnull().sum())
print(data[data['GHI'] <0].count())#check for negative values of GHI, DNI, DHI, ModA, ModB,WS, WSgust)
#NEgative values handling
data['GHI'] = data['GHI'].interpolate(method='linear')
data['GHI'] = data['GHI'].interpolate(method='linear')
