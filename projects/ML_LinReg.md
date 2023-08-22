# Linear Regression og Perceptroner i teori og praksis
Nærværende dokument beskriver et projekt, der vedrører en af de mest simple maskinelæringsalgoritmer kaldet Lineær regression Selvom den er relativt simpel, giver den et super godt indblik i hvad maskinelæring er og hvad det kan bruges til. Ydermere er den en foreløber for en lidt mere avanceret form for regression kaldet logistisk regression. 

## Et simpelt eksempel: 100 meter løb
100 meter løb er en af de klassiske discipliner indenfor atletik. 
Tiden, det tager at løbe de 100 m bliver stadig kortere og kortere. På følgende [side](https://www.worldathletics.org/records/all-time-toplists/sprints/100-metres/outdoor/men/senior) fremgår resultaterne for mænd historisk. Samme sted kan I finde de tilsvarende resultater for kvinder.  

I det følgende skal I skrive et program, der benytter data fra siden herunder dato ud af x-aksen og den daværende verdensrekord op ad y-aksen. 
I skal mere præcist gøre følgende:

- (a) Beregn koefficienterne for den bedste rette linje vha af mindste kvadraters metode. 
- (b) Udregn MSE (mean-squared-error)
- (c) Visualiser den bedste rette linje i et koordinat system
- (d) Hvornår vil vi ifølge modellen være under 9 sek (for mænd og for kvinder)
- (e) Hvad kan problemerne være med denne model?

## Lineær regression i 2D
a) Skriv et program der kan indlæse en simpel tekstfil med to kolonner:

x1 y1<br>
x2 y2<br>
...<br>
xn yn <br>

b) Visualiser punkterne i et koordinatsystem

c) Konstruer en vilkårlig ret linje og lav skydere der kan justere på koefficenterne for linjen 

d) Visualiser MSE ved hjælp af små kvadrater og find den bedste rette linje. 

e) Find en case fra den virkelige verden og prøv at bruge dit program til at bestemme den bedste rette linje. 

f) Brug programmet til at interpolere og ekstrapolere data. Giver dine fund mening?

## Multiple lineær regression
Brug nu multiple lineær regression eller multivariate lineær regression på en selvvalgt case, som du synes kunne være interessant. Det er tilladt at bruge scikit bibliotekt. Eksempel på kode findes i slides. Brug modellen til at forudsige nye værdier. Stemmer det mon overens med udviklingen?

## Polynomiel regression
Brug nu polynomiel regression på en selvvalgt case, som du synes kunne være interessant. Det er tilladt at bruge scikit bibliotekt. Eksempel på kode findes i slides. Brug modellen til at forudsige nye værdier. Stemmer det mon overens med udviklingen?

## Perceptroner i to dimensioner
I det følgende skal du forstå og implementere en simpel perceptron, som er en af de grundlæggende byggesten i neurale netværk. 
Du skal følge guiden [http://iftek.dk/it-sikkerhed-perceptron-algoritmen] og lave en visuel repræsentation, hvor du generer et seperabelt datasæt som det første, og bagefter implementerer perceptronalgoritmen, så den finder en ret linje, der seperarer de to punktmængder. Det er fint bare at finde linjen, men man må også gerne illustrere hvorledes linjen justeres undervejs i algoritmen. 
Det er vigtigt at blive bekendt og velfunderet i perceptroner, da de er centrale byggesten i neurale netværk. Se evt. en P5.JS implementation ved at trykke på [https://editor.p5js.org/henrik.sterner/sketches/LhMDTMS7a]
