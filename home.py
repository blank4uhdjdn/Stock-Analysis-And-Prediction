import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Stock Market Analyzer",
    layout="wide",
    page_icon="📈"
)

# Optional: Use a banner image or logo
# image = Image.open("assets/banner.png")  # You can use your own image
# st.image(image, use_column_width=True)

st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>📈 Stock Market Analyzer</h1>
    <h4 style='text-align: center; color: white;'>Analyze, visualize, and forecast stock performance with ease</h4>
    <hr style='margin-top: 1rem; margin-bottom: 2rem;'>
""", unsafe_allow_html=True)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚀 What You Can Do")
    st.markdown("""
    - 🔍 Search and explore historical stock prices  
    - 📉 View technical charts and moving averages  
    - 🕯️ Generate candlestick charts  
    - 🔮 Forecast future trends with linear models  
    - 📊 See returns, volatility, and more

    """)
    st.success("Use the sidebar ➡️ to begin exploring stocks!")

with col2:
    st.markdown("### 💡 How It Works")
    st.markdown(""""
    1. Go to **Overview** and enter a stock ticker (like `AAPL` or `INFY.NS`)  
    2. Navigate through the dashboards:
        - Technical Charts  
        - Forecasting  
        - Financial Metrics  
    3. Discover insights from historical trends  
    4. Make informed decisions 📊  
    """)
    st.info("Built with 💙 using Streamlit and yFinance")

# Footer
st.markdown("""
<hr>
<p style="text-align: center; font-size: 14px; color: gray;">
Made by Sajid • Powered by Streamlit • Data from Yahoo Finance
</p>
""", unsafe_allow_html=True)
