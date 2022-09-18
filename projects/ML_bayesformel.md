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