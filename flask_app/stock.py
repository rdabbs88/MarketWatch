import requests
import matplotlib.pyplot as plt

def get_stock_data(ticker, api_key):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': ticker,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

def generate_plot(data, ticker):
    time_series = data.get('Time Series (Daily)', {})
    dates = list(time_series.keys())[:30]
    closes = [float(time_series[date]['4. close']) for date in dates]

    plt.figure(figsize=(10, 4))
    plt.plot(dates[::-1], closes[::-1])
    plt.title(f"{ticker.upper()} - Last 30 Days")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_path = f"flask_app/static/plots/{ticker}.png"
    plt.savefig(plot_path)
    return plot_path
