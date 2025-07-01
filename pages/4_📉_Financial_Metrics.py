import streamlit as st

st.title("📉 Financial Metrics")

if "stock_data" in st.session_state:
    df = st.session_state["stock_data"]
    daily_return = df["Close"].pct_change()
    volatility = daily_return.std() * (252 ** 0.5)
    total_return = (df["Close"].iloc[-1] / df["Close"].iloc[0]) - 1

    st.metric("Total Return (%)", f"{total_return * 100:.2f}")
    st.metric("Annualized Volatility", f"{volatility:.2f}")
    st.line_chart(daily_return)
else:
    st.warning("Please load stock data from the Overview page.")
