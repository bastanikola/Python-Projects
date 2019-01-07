-------------------------------------------------------------
### PROJECT: AVOCADO PRICES PREDICTION - FACEBOOK PROPHET ###
-------------------------------------------------------------
-------------------------
### PROBLEM STATEMENT ###
-------------------------
'''
PROBLEM STATEMENT

    - Data represents weekly 2018 retail scan data for National retail volume (units) and price.
    - Retail scan data comes directly from retailers’ cash registers based on actual retail sales of Hass avocados.
    - Starting in 2013, the table below reflects an expanded, multi-outlet retail data set. Multi-outlet reporting includes an aggregation of the following channels: grocery, mass, club, drug, dollar and military.
    - The Average Price (of avocados) in the table reflects a per unit (per avocado) cost, even when multiple units (avocados) are sold in bags.
    - The Product Lookup codes (PLU’s) in the table are only for Hass avocados. Other varieties of avocados (e.g. greenskins) are not included in this table.
    - Some relevant columns in the dataset:

    - Date - The date of the observation
    - AveragePrice - the average price of a single avocado
    - type - conventional or organic
    - year - the year
    - Region - the city or region of the observation
    - Total Volume - Total number of avocados sold
    - 4046 - Total number of avocados with PLU 4046 sold
    - 4225 - Total number of avocados with PLU 4225 sold
    - 4770 - Total number of avocados with PLU 4770 sold
'''
------------------------------
### STEP 1: IMPORTING DATA ###
------------------------------
'''
    - You must install fbprophet package as follows: pip install fbprophet

    - If you encounter an error, try: conda install -c conda-forge fbprophet

    - Prophet is open source software released by Facebook’s Core Data Science team.

    - Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.

    - Prophet works best with time series that have strong seasonal effects and several seasons of historical data.

    - For more information, please check this out: https://research.fb.com/prophet-forecasting-at-scale/ https://facebook.github.io/prophet/docs/quick_start.html#python-api
'''
#import libraries 
import pandas as pd             # Import Pandas for data manipulation using dataframes
import numpy as np              # Import Numpy for data statistical analysis 
import matplotlib.pyplot as plt # Import matplotlib for data visualisation
import random
import seaborn as sns
from fbprophet import Prophet

#dataframes creation for both training and testing datasets 
avocado_df = pd.read_csv('avocado.csv')

-------------------------------------
### STEP 2: EXPLORING THE DATASET ###
-------------------------------------
#Let's view the head and the tail of the training dataset
avocado_df.head()
avocado_df.tail()

avocado_df = avocado_df.sort_values("Date")

plt.figure(figsize=(10,10))
plt.plot(avocado_df['Date'], avocado_df['AveragePrice'])

#Bar Chart to indicate the number of regions 
plt.figure(figsize=[25,12])
sns.countplot(x = 'region', data = avocado_df)
plt.xticks(rotation = 45)

#Bar Chart to indicate the year
plt.figure(figsize=[25,12])
sns.countplot(x = 'year', data = avocado_df)
plt.xticks(rotation = 45)

avocado_prophet_df = avocado_df[['Date', 'AveragePrice']]

-----------------------------------------
### STEP 3: MAKE PREDICTIONS - PART 1 ###
-----------------------------------------
avocado_prophet_df = avocado_df[['Date', 'AveragePrice']]
avocado_prophet_df = avocado_prophet_df.rename(columns={'Date':'ds', 'AveragePrice':'y'})

m = Prophet()
m.fit(avocado_prophet_df)

#Creting a dataframes
future = m.make_future_dataframe(periods=365)
#Forcasting the data
forecast = m.predict(future)

figure = m.plot(forecast, xlabel='Date', ylabel='Average Price', title='Avocado Price Prediction')
figure3 = m.plot_components(forecast)

-----------------------------------------
### STEP 3: MAKE PREDICTIONS - PART 2 ###
-----------------------------------------
#dataframes creation for both training and testing datasets 
avocado_df = pd.read_csv('avocado.csv')

avocado_df_sample = avocado_df[avocado_df['region']=='West']

avocado_df_sample = avocado_df_sample.sort_values("Date")

plt.figure(figsize=(10,10))
plt.plot(avocado_df_sample['Date'], avocado_df_sample['AveragePrice'])

avocado_df_sample = avocado_df_sample.rename(columns={'Date':'ds', 'AveragePrice':'y'})

m = Prophet()
m.fit(avocado_df_sample)
#Forcasting into the future
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)

figure = m.plot(forecast, xlabel='Date', ylabel='Price')
figure3 = m.plot_components(forecast)
