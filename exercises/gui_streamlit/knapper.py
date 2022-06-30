import streamlit as st
# Laver en knap der ikke gør noget
st.button("Tryk på mig for ingen grund")
 
# Tryk på en knap som så viser noget tekst
if(st.button("Tryk her")):
    st.text("Velkommen til!!!")