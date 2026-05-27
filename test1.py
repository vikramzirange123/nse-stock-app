import streamlit as st
import yfinance as yf
import pandas as pd
import sys
# -----------------------------
# NSE STOCK LIST
# -----------------------------

url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

df = pd.read_csv(url)
# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="NSE Stock Dashboard",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📈 NSE Stock Dashboard")

# -----------------------------
# SIDEBAR STOCK LIST
# -----------------------------
st.sidebar.title("NSE Stock List")

@st.cache_data(ttl=60)
def load_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")

selected_stock = st.sidebar.selectbox(
    "Select Stock",
    df["SYMBOL"]
    
)
company_name = df.loc[
    df["SYMBOL"] == selected_stock,
    "NAME OF COMPANY"
].values[0]

# -----------------------------
# STOCK DATA
# -----------------------------
stock_symbol = selected_stock + ".NS"

try:
    stock = yf.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get("currentPrice", "N/A")
    day_high = info.get("dayHigh", "N/A")
    day_low = info.get("dayLow", "N/A")
    previous_close = info.get("previousClose", "N/A")
    open_price = info.get("open", "N/A")

    # -----------------------------
    # DISPLAY DATA
    # -----------------------------
    st.subheader(f"Stock: {selected_stock}")

    st.subheader(f"Stock Name: {company_name}")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Current Price", current_price)

    with col2:
        st.metric("Day High", day_high)

    with col3:
        st.metric("Day Low", day_low)

    #st.divider()

    #col4, col5 = st.columns(2)

    with col4:
        st.metric("Previous Close", previous_close)

    with col5:
        st.metric("Open Price", open_price)

   

except Exception as e:
    st.error(f"Error: {e}")