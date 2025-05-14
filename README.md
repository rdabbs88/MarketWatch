# MarketWatch

Is a web application that allows a user to input stock ticker symbols and it will output real-time stock data and metrics. It can be used as a tool for evaluating whether a stock is moving in an upward or downward trend using technical indicators.

## Website Link
[https://market-watch-beryl.vercel.app/](https://market-watch-beryl.vercel.app/)


## Overview
This web application helps users analyze stock information, by retrieving current and historical data using the Alpha Vantage API. After submitting a valid ticker symbol, the following will be displayed:
- Latest Closing price
- 50-day moving average
- 200-day moving average
- P/E (Price-to-Earnings) ratio

**Why:** These metrics are useful indicators to identify growth or "rocket" stocks, as well as visualizing a stock's upward or downward trend.

## Technology Stack

- **Frontend:**
    - HTML, CSS

- **Backend:**
    - Python, Flask

- **API/Data:**
    - Alpha Vantage (TIME_SERIES_DAILY, OVERVIEW)

- **Data visualization/graphs:** 
    - Matplotlib

- **Website Deployment:** 
    - Vercel