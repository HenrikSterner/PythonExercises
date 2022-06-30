from pandas.core.indexes.datetimes import date_range
import streamlit as st
from datetime import date
import yfinance as yf
import matplotlib.pyplot as plt

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Data Visualizer')
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select stock', stocks)

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
   
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

#Column names are [index,Date,Open,High,Low,Close, Adj Close, Volume]
# you can convert to single dimensinonal list like this
opendata = data["Open"].tolist()
closedata = data["Close"].tolist()
#for x in opendata:
#    st.write(x)

plt.plot(opendata)
plt.ylabel('Open data')
plt.show()
st.pyplot(plt)
