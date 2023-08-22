# Øvelser til matplotlib

* 1. Lav en grundlæggende linjegraf med nogle fiktive datapunkter.
* 2. Opret en stolpediagram over salg for forskellige produkter.
* 3. Lav en cirkeldiagram, der viser fordelingen af emner i en undersøgelse.
* 4. Opret en liniestilkurve med forskellige stilarter og farver.
* 5. Lav en stabelt stolpediagram med flere datasæt.
* 6. Opret en linielabel for at vise flere linjer på samme plot.
* 7. Lav en scatter plot med tilfældige datapunkter.
* 8. Opret en histogram over en samling af tilfældige tal.
* 9. Lav et pie chart for at vise fordelingen af kategorier i en samling af data.
* 10. Opret en vandret stolpediagram med navne på den ene akse og værdier på den anden.
* 11. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()
```
* 12. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 and 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
```
* 13. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);
```
* 14. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5]);
```
* 15. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.axis('tight');
```
* 16. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.axis('equal');
```
* 17. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt

# Opret et nyt Matplotlib-vindue
plt.figure()

# Plot to linjekurver med forskellige farver
plt.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], color="red")
plt.plot([1, 2, 3, 4, 5], [11, 12, 13, 14, 15], color="blue")

# Vis figuren
plt.show()
```
* 18. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt
plt.figure()
plt.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], color="red")
plt.plot([1, 2, 3, 4, 5], [11, 12, 13, 14, 15], color="blue")
plt.show()
```

* 19. Hvad gør følgende kode:
```python
import matplotlib.pyplot as plt
plt.figure()
plt.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], color="red")
plt.plot([1, 2, 3, 4, 5], [11, 12, 13, 14, 15], color="blue")
plt.title("To linjekurver")
plt.xlabel("X-akse")
plt.ylabel("Y-akse")
plt.show()
```
* 20.Opret et nyt Matplotlib-vindue og plot et søjlediagram af to lister med tal.
* 21. Opret et nyt Matplotlib-vindue og plot et linjediagram af to lister med tal.
* 22. Opret et nyt Matplotlib-vindue og plot et cirkeldiagram af to lister med tal.
* 23. Opret et nyt Matplotlib-vindue og plot et histogram af to lister med tal.
* 24. Opret et nyt Matplotlib-vindue og plot et scatter plot af to lister med tal.
* 25. Opret et nyt Matplotlib-vindue og plot et box plot af to lister med tal.
* 26. Opret et nyt Matplotlib-vindue og plot et violin plot af to lister med tal. Lidt hjælp:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(100)
plt.violinplot(x)
plt.show()
``` 
* 27. Opret et nyt Matplotlib-vindue og plot et pie chart af to lister med tal. Lidt hjælp:
```python
import matplotlib.pyplot as plt
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
```
* 28. Opret et nyt Matplotlib-vindue og plot et stem plot af to lister med tal. Lidt hjælp:
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1, 2 * np.pi, 10)
markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')
plt.setp(baseline, color='r', linewidth=2)
plt.show()
```
* 29. Opret et nyt Matplotlib-vindue og plot et polar plot af to lister med tal. Lidt hjælp:
```python
import matplotlib.pyplot as plt
import numpy as np
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, color='r', linewidth=3)
ax.set_rmax(2)
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
```
* 30. Opret et nyt Matplotlib-vindue og plot et 3D plot af to lister med tal. Lidt hjælp:
```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-3.0, 3.0, 0.05)
X, Y = np.meshgrid(x, y)
Z = np.sin(X + Y)
ax.plot_surface(X, Y, Z)
plt.show()
```

* 31. Opret et boxplot af to lister med tal. Lidt hjælp:
```python
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
data = np.random.normal(100, 20, 200)
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
bp = ax.boxplot(data)
plt.show()
```

