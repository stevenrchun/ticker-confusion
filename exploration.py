import yfinance as yf
import pandas as pd

data = yf.download(tickers = "AMCX AMC", period="3mo", interval="1m")
print(data.head())

data.to_csv('amc[x].csv', index = False)



