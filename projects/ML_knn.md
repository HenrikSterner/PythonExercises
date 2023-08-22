# Klassifikation ved brug **K**-Nærmeste-Naboer algoritmen
Nærværende dokument beskriver et projekt, der vedrører en af de mest simple maskinelæringsalgoritmer kaldet K-Nærmeste-Naboer eller bare KNN. Selvom den er relativt simpel, giver den et super godt indblik i hvad maskinelæring er og hvad det kan bruges til. 
## Del I: 1-NN i 2D
I det følgende er målet at implementere en visuel 1-NN, der altså klassificerer et nyt punkt efter sin nærmeste nabo.

1. Lav en class Point, der repræsenterer et punkt som  initialiseres et tilfældigt sted på skærmen og som har en label i form af en farve (rød/blå eller kat/hund…). Dette udgør mængden $$S=\{(x1,y1),…(xn,yn)\}$$
2. Lav en liste af disse Point punkter og visualiser dem på skærmen med forskellige farver
3. Generer nu et nyt punkt p, som du kender placering på men ikke kender label/farve på. 
4. Implementer en funktion 1NN, der finder det nærmest punkt og farvelæg p udfra samme farve som nærmeste nabo
5. Udvid programmet, så det ikke kun består af to farver men et vilkårligt antal.

## Del 2: k-NN i 2D

Lav nu en ny funktion kNN som implementerer kNN-algoritmen, som tager et ulige K (!!) og et punkt p uden label. Antag til at starte med, at et punkt kun kan have to forskellige labels.
Følgende skal gøres:  
1. Beregn den euklidiske distance fra alle andre punkter til p
2. Sorter listen ud fra distancen til p
3. Udvælg de K første punkter fra denne liste
4. Lav en afstemning dvs. find ud af hvilken label der er flest af blandt de K udtagne punkter. 
5. Farvelæg p ud fra dette 
6. Udvid koden så den nu også kan inddrage punkter med flere forskellige labels.
7. Udvælg et virkeligt datasæt bestående af to kolonne med feauteres og 1 kolonne med mulighed for flere labels. Indlæs og afprøv din KNN algoritme på casen. 
8. Konstruer en visualisering af valg af K. Hvor du har K ud af x-aksen og antal korrekte klassificeringer op ad y-aksen. Prøv den af i praksis. 

## Del 3: Forskellige distance metrikker

Indtil nu har vi kun gjort brug af den euklidiske distance. 
I det følgende skal implementeres mindst tre forskellige [distancefunktioner](https://towardsdatascience.com/9-distance-measures-in-data-science-918109d069fa). Tryk på linket for at få nogle eksempler på nogle af disse funktioner. Overvej styrker og svagheder ved disse.

## Del 4: Implementer kNN i numpy
I denne øvelse skal du prøve at implementere kNN i numpy, hvis du har mod på det (dvs. helt frivillig men hvis du har tid til overs så kig på den). Hvis du synes det er for svært, så prøv at forstå følgende kode og prøv den af i praksis:

```python
# Function computing Euclidean distance
def euclidDistance(x1,x2):
    return(np.sqrt(np.sum((x1-x2)**2)))
# Function to calculate KNN
def prediction(xTrain,y,xInput,K):
    predLabels=[]
    for x in xInput:
        distances=[] # to store distances
        for i in range(len(xTrain)):
            distances.append(euclidDistance(np.array(xTrain[i,:]),x))            
        distances=np.array(distances)
        d = np.argsort(distances)[:K] # k first points
        labels = y[d]
        predLabels.append(stats.mode(labels)[0])
    return predLabels
```
Den kræver at du har datasættet liggende. Tjek mappen på github kaldet data.


## Del 5: kNN i praksis 
Anvend kNN på mindst tre forskellige cases. For hver case skal der 
1. Udvælge relevante træningsdata og testdata, som I indlæser. 
2. Separere features og labels for træningsdata og tilsvarende for testdata.
3. Afprøves KNN med mindst to forskellige distancemetrikker  
4. Plottes i matplotlib en graf med k fra 2 til 50 ud af x-aksen og den respektive accuracy score opad y-aksen for den respektive k-værdi.
5. Argumenter for valg af den optimale K. 
6. Overvej hvorledes man kunne lave en vægtet KNN. Dvs. hvor man tager højde for at datapunkterne kan have forskellige vægte (i 2D kunne det illustreres med radier). Prøv at implementer det i praksis. (Frivillig opgave)
  
### Brug 
I må gerne bruge den indbyggede knn - se nedenfor. I vælger selv cases men I kan lade jer inspirere af de datasæt i mine slides. 

Herunder et eksempel på hvorledes man kan indlæse data og afvikle knn først med scikits knn og bagefter med knn ovenfor. 

```python
# Assigning features and label variables
# First Feature
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
# Second Feature
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

# Label or target varible
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

# Import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
weather_encoded=le.fit_transform(weather)
print(weather_encoded)
#Overcast:0, Rainy:1, and Sunny:2.
# printer [2 2 0 1 1 1 0 2 2 1 2 0 0 1]
# converting string labels into numbers
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
#combinig weather and temp into single listof tuples
features=list(zip(weather_encoded,temp_encoded))
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training sets
model.fit(features,label)

#Predict Output
predicted= model.predict([[0,2]]) # 0:Overcast, 2:Mild
print(predicted)
#printer 1
```

Herunder eksempel med den hjemmelavet knn:
```python
# Load data 
path = "data/MNIST-5-6-Subset.txt" #husk at ændre filnavn
data = np.loadtxt(path,dtype = np.float64)
data = data.reshape(1125,784)
path = "data/MNIST-5-6-Subset-Labels.txt"
labels = np.loadtxt(path,dtype = np.int8)

def generateImage(arr):
    two_d = np.transpose((np.reshape(arr, (28, 28)) * 255).astype(np.uint8))
    plt.imshow(two_d, interpolation='nearest')
    return plt

generateImage(data[0]).show() #show the first image

xTrain = data[0:100]
yTrain = labels[0:100]
xTest = data[100:120]
yTest = labels[100:120]
yPred = prediction(xTrain,yTrain,xTest , 75)
# Check accuracy
accuracy_score(yTest, yPred)
```

Endelig også et eksempel hvor I bruger indbyggede datasæt (iris):
```python
from sklearn.datasets import load_iris
iris = load_iris()
# Storing the data and labels into "X" and "y" varaibles
X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
from sklearn.neighbors import KNeighborsClassifier

# We “assumed” k(the number of neighbors i.e. n_neighbors)  = 3. It can also be 5, 7 … 10
model = KNeighborsClassifier(n_neighbors=3)
# Training or fitting the model with the train data
model.fit(X_train,y_train)

model.predict(X_test) 
model.score(X_test,y_test)

```
Herunder lidt om features og labels for iris-sættet. 

Features:
* sepal length in cm
* sepal width in cm
* petal length in cm
* petal width in cm

Labels:
* “0”: setosa
* “1”: versicolor
* “2”: virginica