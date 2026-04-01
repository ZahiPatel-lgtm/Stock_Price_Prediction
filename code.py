import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="Indian Stock Tracker", layout="wide")

# --- NEW: DATE & TIME SECTION ---
now = datetime.now()
# Formatting: Day-Month-Year | Hour:Minute:Second
current_time = now.strftime("%d %B %Y | %H:%M:%S")

st.title("📈 Stock Tracker & Predictor")
st.write(f"**Last Updated:** {current_time}")
st.write("This app uses a **Moving Average** to guess tomorrow's price and converts USD to ₹ automatically.")

# 2. Sidebar Settings
st.sidebar.header("Market Settings")
ticker = st.sidebar.text_input("Stock Symbol (e.g., RELIANCE.NS, TSLA)", "RELIANCE.NS")
window = st.sidebar.slider("Average Window (Days)", 2, 30, 5)

# 3. Fetch Data & Exchange Rate
data = yf.download(ticker, period="60d")
exchange_data = yf.download("USDINR=X", period="1d")
usd_to_inr = float(exchange_data['Close'].iloc[-1])

if not data.empty:
    # --- CLEANING DATA ---
    df_cleaned = data[['Close']].dropna()
    raw_prices = df_cleaned['Close'].values.flatten().tolist()
    
    # --- CURRENCY CONVERSION ---
    if not (ticker.upper().endswith(".NS") or ticker.upper().endswith(".BO")):
        prices = [p * usd_to_inr for p in raw_prices]
        currency_label = f"Price (₹) - Converted from USD"
    else:
        prices = raw_prices
        currency_label = "Price (₹) - Direct NSE/BSE"

    current_price = prices[-1]

    # --- MATH LOGIC ---
    prev_avg = sum(prices[-window-1 : -1]) / window
    error = abs(prev_avg - current_price) / current_price
    accuracy_score = (1 - error) * 100

    prediction = sum(prices[-window:]) / window
    price_diff = prediction - current_price

    # 4. Dashboard UI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Price", f"₹{current_price:,.2f}")
        
    with col2:
        st.metric("Predicted Tomorrow", f"₹{prediction:,.2f}", delta=f"{price_diff:.2f}")
        
    with col3:
        st.metric("Model Accuracy", f"{accuracy_score:.1f}%")

    # 5. CHART SECTION
    st.subheader(f"{ticker} Price Trend (INR)")
    chart_df = pd.DataFrame(prices, index=df_cleaned.index, columns=[currency_label])
    st.line_chart(chart_df)

    # 6. Status Message
    if accuracy_score > 95:
        st.success(f"The trend for {ticker} is steady. High confidence in this average.")
    else:
        st.warning(f"The market for {ticker} is jumpy. Use this average with caution!")

else:
    st.error("Could not find data. Tip: Use 'RELIANCE.NS' for NSE or 'TSLA' for US stocks.")