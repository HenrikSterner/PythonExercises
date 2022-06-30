# Øvelse

I denne øvelse skal vi prøve at få en python-version af p5 installeret.

1) Åbn Visual Studio Code.
2) Åbn et terminal-vindue.
3) Tjek om du har python installeret ved at eksekvere følgende kommando i terminalen:
```bash
python --version
```
Hvis der gives en fejl, har du ikke `pip` installeret ved at eksekvere følgende kommando i terminalen.
4) Tjek om du har pythons pakke-værktøj pip installeret:
```bash
pip --version
```
Hvis der gives en fejl, har du ikke `pip` installeret.
5) Installér pakken *p5*:
```bash
pip install p5 --user
```
6) Lav en python-fil, der bruger p5. Du kunne f.eks. kalde den *test.py* og indsætte følgende p5-program:
```python
from p5 import *

def setup():
    size(640, 360)
    no_stroke()
    background(204)

def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle_size = random_uniform(low=10, high=80)

    circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    background(204)

run()
```
7) Kør programmet enten fra Visual Studio Code eller fra terminalen med følgende kommando:
```
python test.py
```
