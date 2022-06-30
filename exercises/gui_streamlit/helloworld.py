import streamlit as st
# Henter navn fra tekstboks
name = st.text_input("Navn", "Skriv det her ...")
# printer navn...
if(st.button('OK')):
    result = name.title()
    st.text(result)