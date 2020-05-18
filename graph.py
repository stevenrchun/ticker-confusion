import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

data = yf.download(tickers = "AMCX AMC", period="3mo", interval="5m")
print(data.head())

for col in data.columns:
    print(col)
data['Adj Close']['AMCX'].plot()
data['Adj Close']['AMC'].plot()
plt.savefig('line_plot.png')  
