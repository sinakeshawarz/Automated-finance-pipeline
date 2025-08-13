import yfinance as yf
import pandas as pd
from datetime import datetime

# Define the forex pair (EURUSD) and time period
ticker = 'EURUSD=X'  # Yahoo symbol for EUR/USD
start_date = '2024-01-01'  # Adjust as needed
end_date = datetime.today().strftime('%Y-%m-%d')  # Today

# Fetch historical data
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate daily returns (percentage change in Close price)
data['Daily_Return'] = data['Close'].pct_change() * 100

# Calculate 50-day simple moving average (SMA)
data['50_SMA'] = data['Close'].rolling(window=50).mean()

# Drop rows with NaN (e.g., first few for SMA)
data = data.dropna()

# Save to CSV in the repo root
output_file = 'eurusd_analysis.csv'
data.to_csv(output_file)
print(f'Saved analysis to {output_file}')
