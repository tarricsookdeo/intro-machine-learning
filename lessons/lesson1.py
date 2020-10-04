import pandas as pd
import quandl

from local_settings import *

# Configure Quandl API key
quandl.ApiConfig.api_key = api_key

# Get stock data, and store into a Pandas dataframe
df = quandl.get('WIKI/FB')

# Define which default features inside of the dataframe we want
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Calculate new features based on data returned
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / \
    df['Adj. Open'] * 100.0

# Define new dataframe with calculated features and default features
df = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

print(df.head())
