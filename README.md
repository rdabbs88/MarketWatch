# MarketWatch

Is a web application that allows a user to input stock ticker symbols and it will output real-time stock data and metrics. It can be used as a tool for evaluating whether a stock is moving in an upward or downward trend using technical indicators.

## Website Link
[https://market-watch-beryl.vercel.app/](https://market-watch-beryl.vercel.app/)


## Project Development Journey

- **Step 1:** Initial Project Research, Data Analysis, and Website Development
    - Github link: [https://github.com/rdabbs88/StockMarketAnalyzer](https://github.com/rdabbs88/StockMarketAnalyzer)
- **Step 2:** Improving Website and AWS Deployment
    - Github link: [https://github.com/rdabbs88/MarketAnalyzerWebsite](https://github.com/rdabbs88/MarketAnalyzerWebsite)
- **Step 3:** UI Improvements and Vercel Hosting
    - Current project

## Overview
This web application helps users analyze stock information, by retrieving current and historical data using the Alpha Vantage API. After submitting a valid ticker symbol, the following will be displayed, which are also visualized through a graph:
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

## Rate Limiting and API Efficiency
Due to Alpha Vantage's free-tier rate limit (max of 5 requests per minute and 500 per day), I implemented the following to help reduce API requests and prevent being rate-limited:
- A local cache is implemented in-memory, to store data for a given ticker and date combination. This ensure that repeated lookups for the same stock on the same day won't trigger redudant API requests
- Use of the time function [time.sleep(12)] from the time module to throttle request speed

**Why:** These optimizations help reduce the risk of hitting API rate limits