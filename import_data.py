import config as secrets
import yfinance as yf
from tiingo import TiingoClient
import pandas as pd

# Set up Tiingo clinet
tiingo_config = {'api_key': secrets.api_key, 'session': True}

client = TiingoClient(tiingo_config)

# Download minute level data for
# * AMC Entertainment (AMC, theaters)
# * AMC Networks (AMCX, TV shows)
# * Vanguard S&P 500 (VOO, literally everything)

for ticker in ['AMC', 'AMCX', 'VOO']:
    history = client.get_dataframe(ticker,
                                   frequency='10Min',
                                   startDate='2020-05-01',
                                   endDate='2020-05-15')
    # Save to file
    history.to_csv("{}_history.csv".format(ticker), index=True)

# YFinance option.
# data = yf.download(  # or pdr.get_data_yahoo(...
#     # tickers list or string as well
#     tickers="AMC AMCX SPY",
#
#     # use "period" instead of start/end
#     # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#     # (optional, default is '1mo')
#     period="1mo",
#
#     # fetch data by interval (including intraday if period < 60 days)
#     # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#     # (optional, default is '1d')
#     interval="5m",
#
#     # group by ticker (to access via data['SPY'])
#     # (optional, default is 'column')
#     group_by='ticker',
#
#     # use threads for mass downloading? (True/False/Integer)
#     # (optional, default is True)
#     threads=True,
# )
#
# data.to_csv("yf_data.csv", index=True)
