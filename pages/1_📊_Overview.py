import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📊 Overview")

ticker = st.text_input("Enter Ticker (e.g., AAPL, TSLA, INFY.NS)", "AAPL").upper()
start = st.date_input("Start Date", pd.to_datetime("2022-01-01"))
end = st.date_input("End Date", pd.to_datetime("today"))

if ticker:
    data = yf.download(ticker, start=start, end=end, auto_adjust=False)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    st.write(data.tail())
    st.line_chart(data["Close"])
    st.session_state["stock_data"] = data

