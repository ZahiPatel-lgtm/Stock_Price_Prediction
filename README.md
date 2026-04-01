# Stock Price Predictor 📈

This is a project made as a simple website that helps you track stock prices (like Reliance or Tesla) and tries to guess what the price will be tomorrow.

## What does this project do?
- **Real Data:** It pulls live stock prices from the internet (Yahoo Finance).
- **Auto Currency:** If you search for a US stock like "TSLA", it automatically changes the price from Dollars to Indian Rupees (₹).
- **The Prediction:** It uses a "Moving Average." This means it takes the average price of the last few days to guess tomorrow's price. (No complex AI, just simple math!)
- **Accuracy Score:** It tells you how much you can trust the guess by comparing past averages to real prices.
- **Cool Charts:** It shows a nice blue line graph of the price trend.

## How to use it
1. **Stock Symbol:** Type the name of the stock in the sidebar. 
   - For Indian stocks, add `.NS` at the end (Example: `RELIANCE.NS` or `TCS.NS`).
   - For US stocks, just type the name (Example: `TSLA` or `AAPL`).
2. **Average Window:** Use the slider to choose how many days of data the "math" should use.
3. **Live Time:** The app shows the exact date and time you checked the price.

## How to run it on your computer
First, you need to install these three things in your terminal:
```bash
pip install streamlit yfinance pandas