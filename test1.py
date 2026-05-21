import streamlit as st
import yfinance as yf

# Page title
st.set_page_config(page_title="NSE Stock Viewer", layout="centered")

st.title("📈 NSE Stock High/Low Viewer")
@st.cache_data(ttl=5)
def load_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")

# User input
stock_input = st.text_input(
    "Enter NSE Stock Symbol",
    value="RELIANCE"
)

# Button
if st.button("Get Stock Data"):

    # Add .NS automatically
    stock_symbol = stock_input.upper()

    if not stock_symbol.endswith(".NS"):
        stock_symbol += ".NS"

    try:
        # Fetch stock data
        stock = yf.Ticker(stock_symbol)
        info = stock.info

        current_price = info.get("currentPrice", "N/A")
        day_high = info.get("dayHigh", "N/A")
        day_low = info.get("dayLow", "N/A")
        previous_close = info.get("previousClose", "N/A")

        # Display results
        st.success(f"Data for {stock_symbol}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Current Price", current_price)
            st.metric("Day High", day_high)

        with col2:
            st.metric("Previous Close", previous_close)
            st.metric("Day Low", day_low)

    except Exception as e:
        st.error(f"Error: {e}")