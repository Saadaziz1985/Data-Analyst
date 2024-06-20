import yfinance as yf
import pandas as pd
from datetime import datetime
import os

## Define the list of tickers
tickers = ['^GSPC', '^DJI', '^IXIC', '^NYA', '^XAX']

## Set the end date to today
end_date = datetime.today()

## Set the start date to 2 years ago
start_date = '2000-01-01'

## Create an empty DataFrame to store the close prices
close_df = pd.DataFrame()

## Download the close prices for each ticker
for ticker in tickers:
    data = yf.download(ticker, start = start_date, end = end_date)
    close_df[ticker] = data['Close']

## Set the output folder path
#output_folder = r"C:\Users\Saad Aziz\Downloads\Data Source Python"

## Export the DataFrame to Excel
#output_file = os.path.join(output_folder, 'stock_prices.csv')
close_df.to_csv('stock_prices.csv')
