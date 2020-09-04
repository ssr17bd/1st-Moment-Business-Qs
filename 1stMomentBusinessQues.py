# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:07:16 2020

@author: Shaila Sarker
"""

import pandas as pd
salesData = pd.read_csv("D:/DS/1. Sales Analysis - 1st moment/SalesData.csv", encoding= 'unicode_escape') #unicodeDecodeErrVanished

#Exploratory Data Analysis
#Measures of Central Tendency / First moment business decision
salesData.SALES.mean() 
salesData.SALES.median()
#salesData.SALES.mode() #used for categorical data

# Measures of Dispersion / Second moment business decision
salesData.SALES.var() # variance
salesData.SALES.std()#standard deviation
range = max(salesData.SALES) - min(salesData.SALES) # range
range

#Graphical Representation
import matplotlib.pyplot as plt
import numpy as np

plt.bar(height = salesData.SALES, x = np.arange(1,2824,1)) # initializing the parameter [meaningless >> showing the dataset as it is]

plt.hist(salesData.SALES) #histogram or frequency plot [x-axis >> salesAmount, y-axis >> frequency]

plt.boxplot(salesData.SALES) #boxplot [finds out the outliers]
