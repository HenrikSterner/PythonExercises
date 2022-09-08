# Klassifikation ved brug **K**-Nærmeste-Naboer algoritmen
Nærværende dokument beskriver et projekt, der vedrører en af de mest simple maskinelæringsalgoritmer kaldet K-Nærmeste-Naboer eller bare KNN. Selvom den er relativt simpel, giver den et super godt indblik i hvad maskinelæring er og hvad det kan bruges til. 
## Del I: 1-NN i 2D
I det følgende er målet at implementere en visuel 1-NN, der altså klassificerer et nyt punkt efter sin nærmeste nabo.

1. Lav en class Point, der repræsenterer et punkt som  initialiseres et tilfældigt sted på skærmen og som har en label i form af en farve (rød/blå eller kat/hund…). Dette udgør mængden $$S=\{(x1,y1),…(xn,yn)\}$$
2. Lav en liste af disse Point punkter og visualiser dem på skærmen med forskellige farver
3. Generer nu et nyt punkt p, som du kender placering på men ikke kender klassen/ på
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

## Del 3: Forskellige distance metrikker

Indtil nu har vi kun gjort brug af den euklidiske distance. 
I det følgende skal implementeres mindst tre forskellige [distancefunktioner](https://towardsdatascience.com/9-distance-measures-in-data-science-918109d069fa). Tryk på linket for at få nogle eksempler på nogle af disse funktioner. Overvej styrker og svagheder ved disse.

## Del 4: Implementer kNN i numpy
I denne øvelse skal du implementere kNN i numpy. Du skal stadig lave det fra bunden. Hvis du synes det er for svært, så prøv at forstå følgende kode og prøv den af i praksis:

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
- 1. Afprøves mindst to forskellige distancemetrikker og 
- 2. Plottes i matplotlib en graf med k fra 2 til 50 ud af x-aksen og den respektive accuracy score opad y-aksen for den respektive k-værdi. 

I må gerne bruge den indbyggede knn - se nedenfor. Den første case kunne passende være på MNIST datasættet, som ligger under Data på https://github.com/HenrikSterner/PythonExercises/ under projekter. 

Herunder et eksempel på hvorledes man kan indlæse data og afvikle knn:
```python
# Load data 
path = "data/MNIST-5-6-Subset.txt" #husk at ændre filnavn
data = np.loadtxt(path,dtype = np.float64)
data = data.reshape(1877,784)
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