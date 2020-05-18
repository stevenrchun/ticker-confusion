import yfinance as yf
import pandas as pd

data = yf.download(tickers = "AMCX AMC", period="1mo", interval="5m")
print(data)

data.to_csv('amc[x].csv', index = False)



