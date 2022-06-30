import streamlit as st

st.title("Simulation[tm]")
st.write("Here is our super important simulation")

x = st.slider('Slope', min_value=1, max_value=24, step=1)


#adding a histogram
values =[]
for i in range(0,x):
    values.append(i)
st.bar_chart(values)
