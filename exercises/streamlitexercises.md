# Forslag til opgaver
* Lav promilleberegner i Streamlit
* Lav en CPR-validering i Streamlit
* Lav en valutaomregner i Streamlit
* Lav en randomiseret quote/citat generator i Streamlit
* Lav en lommeregner i Streamlit
* Lav et program der viser billeder i Streamlit
* Lav en todo-liste i Streamlit
* Lav en bmi-beregner i Streamlit
* Lav grafer af funktioner i Streamlit
* Lav en kort applikation i Streamlit
* Lav en applikation der viser data fra Danmarks Statistik i Streamlit
* Lav en kalorieberegner i Streamlit
* Lav en applikation der gemmer data i Streamlit
* Lav en applikation der henter data i Streamlit
* Lav en applikation der viser billeder i Streamlit
* Ordoptælling: Opret en applikation, der tager en tekst som input og viser antallet af ord, sætninger og tegn i teksten.
* Farvepaletgenerator: Opret en applikation, der genererer en tilfældig farvepalet baseret på brugerens valg af farveskala og antal farver.
* Spørgeundersøgelse: Lav en enkel spørgeundersøgelse, hvor brugere kan besvare nogle spørgsmål ved hjælp af forskellige input-widgets som tekstinpt, radioknapper eller flervalgsfelter.
* Portfolio Tracker: Lav en enkel applikation, hvor brugere kan indtaste aktier eller kryptovalutaer, de ejer, og applikationen viser den aktuelle værdi baseret på realtime-markedsdata.
* Tipkalkulator: Lav en kalkulator, der beregner et anbefalet tipbeløb baseret på den samlede regning og en procentdel.
* Lav en applikation der viser en video i Streamlit. Man kan evt. bruge [OpenCV](https://opencv.org/) til at vise videoen. Herunder et eksempel: 
```python
import cv2
import streamlit as st
import numpy as np
import time

st.title('Webcam Live Feed')
run = st.checkbox('Run')

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

```



