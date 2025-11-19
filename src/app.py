import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

# main

st.title("Crypto Live Plot")
st.write("Welcome to my dashboard")

# load data by api

def load_data(ticker):

    stock = yf.Ticker(ticker)
    data = stock.history(period='1y')
    return data

tickers_list = ['BTC-USD', 'ETH-USD', 'DOGE-USD', 'SHIB-USD', 'ADA-USD']
tikcer = st.sidebar.selectbox('Choose Ticker:', tickers_list)
df = load_data(tikcer)

df['SMA50'] = df['Close'].rolling(window=50).mean()

# plot

if not df.empty:
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    ),
    go.Scatter(
        x=df.index,
        y=df['SMA50'],
        mode='lines',
        name='50 days mean',
        line=dict(color='blue', width=1.5)
    )
    ])
    st.plotly_chart(fig)
else:
    st.error('No Data Found!')