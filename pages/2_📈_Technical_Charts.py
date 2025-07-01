import streamlit as st
import plotly.graph_objs as go

st.title("📈 Technical Charts")

if "stock_data" in st.session_state:
    df = st.session_state["stock_data"]
    ma_days = st.slider("Moving Average Days", 5, 100, 20)
    df[f"MA_{ma_days}"] = df["Close"].rolling(ma_days).mean()
    st.line_chart(df[[f"MA_{ma_days}", "Close"]])

    st.subheader("🕯️ Candlestick Chart")
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )])
    st.plotly_chart(fig)
else:
    st.warning("Please load stock data from the Overview page.")
