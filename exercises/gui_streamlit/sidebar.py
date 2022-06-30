import streamlit as st
st.sidebar.header("Features")
st.sidebar.markdown("Drag the sliders")

row = st.sidebar.slider("Display:",0,100,50)


if st.checkbox("Show something"):
    st.write("Hej")    