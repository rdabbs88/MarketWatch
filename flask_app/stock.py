import requests
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime
import os

os.environ["MPLCONFIGDIR"] = "/tmp"

# add a cache to help with rate limit issues
# key = (ticker, date), value = repsonse dict
stock_cache = {}

def get_stock_data(ticker, api_key):

    today = datetime.today().date()
    cache_key = (ticker, today)

    # Check if the ticker has been cached
    if cache_key in stock_cache:
        print(f"Using cached data for {ticker}")
        return stock_cache[cache_key]
    
    print(f"Fetching new data for {ticker}")

    # First API call, get historical data for moving averages
    url_prices = "https://www.alphavantage.co/query"
    params_prices = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "outputsize": "full",
        "apikey": api_key
    }
    r = requests.get(url_prices, params=params_prices)
    #data = r.json().get("Time Series (Daily)", {})
    json_prices = r.json()

    # check rate limit
    if "Note" in json_prices or "Error Message" in json_prices:
        print("FAILED: rate limited or error message in TIME_SERIES_DAILY")
        return None

    # print(json_prices)
    data = json_prices.get("Time Series (Daily)", {})

    if not data:
        print("FAILED: no price data found")
        return None
    
    df = pd.DataFrame(data).T
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df["close"] = df["4. close"].astype(float)
    print(df.columns)

    # Calculate 50- and 200-day MAs
    df["ma_50"] = df["close"].rolling(window=50).mean()
    df["ma_200"] = df["close"].rolling(window=200).mean()

    latest = df.iloc[-1]

    # Add a delay to prevent rate limits
    time.sleep(12)

    # Second API call, get P/E Ratio from company overview
    url_pe = "https://www.alphavantage.co/query"
    params_pe = {
        "function": "OVERVIEW",
        "symbol": ticker,
        "apikey": api_key
    }
    r_pe = requests.get(url_pe, params=params_pe)
    pe_data = r_pe.json()

    # check for rate limit again
    if "Note" in pe_data or "Error Message" in pe_data:
        print("FAILED: rate limited or error message in OVERVIEW call")
        return None

    pe_ratio = pe_data.get("PERatio", "N/A")

    result = {
        "df": df,
        "latest_price": latest["close"],
        "ma_50": latest["ma_50"],
        "ma_200": latest["ma_200"],
        "pe_ratio": pe_ratio
    }

    # Save the result to cache
    stock_cache[cache_key] = result

    return result


def generate_plot(data, ticker):
    df = data["df"]
    plt.figure(figsize=(10, 4))
    plt.plot(df.index[-30:], df["close"].tail(30), label="Close Price")
    plt.plot(df.index[-30:], df["ma_50"].tail(30), label="MA 50", linestyle="--")
    plt.plot(df.index[-30:], df["ma_200"].tail(30), label="MA 200", linestyle="--")
    plt.legend()
    plt.title(f"{ticker.upper()}: 30-Day Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_path = f"flask_app/static/plots/{ticker}.png"
    plt.savefig(plot_path)
    return plot_path