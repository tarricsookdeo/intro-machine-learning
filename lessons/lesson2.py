import math

import pandas as pd
import quandl

from local_settings import *

# Configure Quandl API key
quandl.ApiConfig.api_key = api_key

# Get stock data, and store into a Pandas dataframe
df = quandl.get('WIKI/GOOGL')

# Define which default features inside of the dataframe we want
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Calculate new features based on data returned
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / \
    df['Adj. Open'] * 100.0

# Define new dataframe with calculated features and default features
df = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

# Used so later on only this variable has to be changed
forecast_col = 'Adj. Close'

# Fills in na data with obsurd value so it can be treated as an outlier
df.fillna(-99999, inplace=True)

# How far out to predict price
forecast_out = int(math.ceil(0.01 * len(df)))

# Creates label row and places it to the back of the dataframe
df['label'] = df[forecast_col].shift(-forecast_out)

# Removes na values
df.dropna(inplace=True)

print(df.tail())
