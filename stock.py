import yfinance as yf
msft = yf.Ticker("MSFT")
#To view n day past market data
#In this exammple n = 6
print(msft.history(period="5d")) 

#to plot n day graph
import matplotlib.pyplot as plt
import seaborn

hist(['Close'].plt(figsize=(16,9)))
