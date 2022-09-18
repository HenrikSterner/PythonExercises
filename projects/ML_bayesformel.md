# Klassifikation ved brug Bayes sætning/formel
Nærværende dokument beskriver et projekt, der vedrører en af de mest simple maskinelæringsalgoritmer, som anvender Bayes formel. Den er simpel og elegant, men ret effektiv når datasæt bliver tilpas store. 

## 1) Implementer Bayes formel med en feature data og 1 label
Ligesom slides skal vi starte med at implementere den mest simple udgave af Bayes formel hvor vi kun har en feature og label. 

## 2) Anvend Bayes formel  på et eksempel
I denne del skal du afprøve Bayes formel i praksis ved at indlæse en fil med to kolonner. Feature i første kolonne og label i anden kolonne. 
Man kan evt tage udgangspunkt i de data omkring vejr og hvorvidt man bør spille, men prøv gerne at finde nogle data selv.


## 3) Implementer multidimensional variant af Bayes formel og 1 label
I det følgende skal implementeres den multidimensionale variant med 1 label.
Resultatet skal vise sandsynligheder for alle cases.  

## 4) Anvend den multidimensionelle Bayes formel på et selvvalgt datasæt
I denne del skal du afprøve Bayes formel i praksis ved at indlæse en fil med to kolonner. Feature i første kolonne og label i anden kolonne. 
Man kan evt tage udgangspunkt i de data omkring vejr og hvorvidt man bør spille, men prøv gerne at finde nogle data selv.

## 5) Tekstklassifikation
Afprøv nu din algoritme på sentiment analyse af twitter beskeder. Tag udgangspunkt i følgende datasæt: <https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis> hvor du I første omgang renser den fra neutrale indlæg. 
Målet er klassificere nye beskeder som enten positive eller negative via dit program fra 4. For at det skal kunne lade sig gøre bør man først analysere de eksisterende beskeder ud fra nogle data såsom længden af teksten, brugen af bestemte ord, gennemsnitlige længde af de enkelte ord, antallet af specieltegn, frekvensen af ord osv. Herunder eksempel på hvorledes man kan udlede frekvensen af ord:

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
[‘and’, ‘document’, ‘first’, ‘is’, ‘one’, ‘second’, ‘the’, ‘third’, ‘this’]
print(X.toarray())
```
Printer følgende ud: 
```python
[[0 1 1 1 0 0 1 0 1]
 [0 2 0 1 0 1 1 0 1]
 [1 0 0 1 1 0 1 1 1]
 [0 1 1 1 0 0 1 0 1]]
 ```


 ## 6) Fake news detektion
 Nu prøver vi Bayes formel af på detektion af fake news fra datasættet: <https://www.uvic.ca/ecs/ece/isot/datasets/fake-news/index.php>. 
 Da datasættet er ret stort kan det være nødvendigt kun at læse nogle af dataene. 



## Bilag
 Hvis man gerne vil teste op mod scikits version, så virker det således:

### Eksempel med flere features men kun en label
 ```python
 # Assigning features and label variables
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
```

Vi kan indkode data i tal således:
```python
# Import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
wheather_encoded=le.fit_transform(wheather)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print "Temp:",temp_encoded
print "Play:",label
print "Wheater:", wheather_encoded
```
Dataene kan sættes ind i en tuple:
```python
#Combinig weather and temp into single listof tuples
features=zip(weather_encoded,temp_encoded)
print features
```

Herefter kan vi prøve Bayes af således:

```python
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features,label)

#Predict Output
predicted= model.predict([[0,2]]) # 0:Overcast, 2:Mild
print "Predicted Value:", predicted
```
### Eksempel med flere features og flere labels
Her et eksempel på det multinominelle tilfælde:

```python
#Import scikit-learn dataset library
from sklearn import datasets

#Load dataset
wine = datasets.load_wine()

# print the names of the 13 features
print "Features: ", wine.feature_names

# print the label type of wine(class_0, class_1, class_2)
print "Labels: ", wine.target_names
# print data(feature)shape
wine.data.shape 
# print the wine labels (0:Class_0, 1:class_2, 2:class_2)
print wine.target
```

Vi splitter op i træning og testdata:

```python
# Import train_test_split function
from sklearn.cross_validation import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=109) # 70% training and 30% test
```

Vi kan træne og afprøve vores model:

```python
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)
```
Samt evaulere nøjagtigheden:

```python
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
```

