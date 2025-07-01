import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🔮 Forecasting")

if "stock_data" in st.session_state:
    df = st.session_state["stock_data"].dropna()
    df['Date_num'] = np.arange(len(df))
    model = LinearRegression()
    model.fit(df[['Date_num']], df['Close'])
    future = np.arange(len(df), len(df)+10).reshape(-1, 1)
    preds = model.predict(future)
    forecast_dates = pd.date_range(df.index[-1] + pd.Timedelta(days=1), periods=10, freq='B')
    forecast_df = pd.DataFrame({"Date": forecast_dates, "Forecast": preds}).set_index("Date")

    st.line_chart(pd.concat([df[['Close']], forecast_df], axis=1))
else:
    st.warning("Please load stock data from the Overview page.")
