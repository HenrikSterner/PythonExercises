import streamlit as st
import time
import datetime
from datetime import datetime, date, time

st.header("Official Date Picker")
st.date_input('start date')
st.date_input('end date')
st.write(f"x={x} y={y}")
st.pyplot()
