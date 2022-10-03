import streamlit as st
from main import login, getStudents
import pandas as pd
import random

st.set_page_config(
    page_title="Lectio",
    page_icon="🏫",
)

st.title("Lectio tilfældighedsgenerator 🎲")

loggedIn = False

if not loggedIn:
    st.subheader("Indsat venligst dine Lectio oplysninger nedenfor")

    st.text_input("Brugernavn", key="username", type="default")
    st.text_input("Kodeord", key="password", type="password")

    if st.button("Indsend ✈️"):
        loggedIn = True

if loggedIn:
    st.subheader("Elever 👨‍🎓")

    username = st.session_state.username
    password = st.session_state.password

    session = login(username, password)
    elever = getStudents(session)

    elevTabel = pd.DataFrame(
        {
            "Elever": elever,
        }
    )

    st.dataframe(elevTabel)

    st.subheader("Dagens heldige elev ✨")
    st.write(random.choice(elever))
