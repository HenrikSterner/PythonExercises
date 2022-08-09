# Klassifikation ved brug **K**-means algoritmen
Nærværende dokument beskriver et projekt, der vedrører en af de mest simple maskinelæringsalgoritmer kaldet K-means . Selvom den er relativt simpel, giver den et super godt indblik i hvad maskinelæring er og hvad det kan bruges til. 
## Del I: Forarbejde til K-means i 2D
I det følgende er målet at implementere en visuel k-means algoritme, der altså segmenterer to sæt af punkter

1. Lav en class Point, der repræsenterer et punkt som  initialiseres et tilfældigt sted på skærmen og som har en label i form af en farve (rød/blå eller kat/hund…). Dette udgør mængden $$S=\{(x1,y1),…(xn,yn)\}$$
2. Lav en liste af disse Point punkter og visualiser dem på skærmen med forskellige farver
3. Implementer en funktion der konstruerer nogle klynge lignende strukturer for hver unik label. Dvs. ensfarvet punkter bør være i samme klynge, men der kan godt forekomme overlap mellem klyngerne. Det kan gøres ved at bruge en tilfældighedsgenerator eller intervaller for punkterne. 
4. Udvid funktionen i 3. så man kan specificere ud fra mindst tre niveauer hvor adskilte klyngerne skal være. 


## Del 2: k-means i 2d
K-means handler om at finde centrummer for klyngerne og algoritmen forløb kort fortalt således:
1. Vælg antallet af clusters k
2. Vælg tilfældige centroider for hvert cluster
3. Tildel alle punkter til deres nærmeste cluster
4. Beregn centroider for de ny clusters
5. Fortsæt med at gentage punkt 3. og 4. 

Stop kun i et af følgende tre tilfælde:
- Centroiderne ændres ikke
- Punkterne bliver i samme cluster
- Det maksimale antal iterationer er nået

I denne del af opgaven skal I implementere og visualisere algoritmen i 2d. Alle tre stop-kritierier skal implementeres.

## Del 3: Implementer k-means i numpy
I denne øvelse skal du implementere k-means i numpy. Du skal stadig lave det fra bunden. 

## Del 4: Hvor gode klynger får vi?
Til at afgøre hvor gode klynger k-means konstruerer, bruges Dunn index og inertia.

- Inertia: Summen af distancer fra alle punkter i et cluster til dens centroide. Hvad Hvad bør værdien være for en god cluster?
- Dunn index: Tager også distancen mellem to clustere i betragtning (tommelfingerregel: jo højere DI jo bedre clustering ).

Implementer to funktioner til at måle disse værdier. 



## Del 5: kmeans i praksis 
Anvend k-means på mindst tre forskellige cases. For hver case skal der 
- 1. Afprøves mindst to forskellige distancemetrikker og 
- 2. Plottes i matplotlib en graf med k fra 2 til 50 ud af x-aksen og det respektive Dunn index samt inertia opad y-aksen for den respektive k-værdi. 

I må gerne bruge den indbyggede knn. 
