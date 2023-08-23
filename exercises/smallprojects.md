# Lidt større projekter for begyndere i Python

Øvelserne herunder er lidt større projekter. Men stadig relativt nemme at implementere. Har man arbejdet med streamlit vil det være rigtig fint at lave en webapp ud af nogle af disse øvelser.

## 1. Gæt et tal
Lav et program, der genererer et tilfældigt tal mellem 1 og 100. Lad brugeren gætte tallet, og fortæl om det er for højt eller for lavt. Lad brugeren gætte indtil det er rigtigt.

## 2. Andengradsligning
Lav et program, der kan løse andengradsligninger. Programmet skal tage tre input fra brugeren: a, b og c. Programmet skal så løse ligningen ax^2 + bx + c = 0. Programmet skal kunne håndtere, at der ikke er nogen løsning, at der er en løsning og at der er to løsninger.

## 3. Kalender
Lav et program, der kan vise en kalender for et givent år og måned. Programmet skal tage to input fra brugeren: år og måned. Programmet skal så vise en kalender for den pågældende måned. Programmet skal også kunne vise en kalender for hele året.

## 4. Dagbog
Lav et program, der kan bruges som en dagbog. Programmet skal kunne tage input fra brugeren og gemme det i en fil. Programmet skal også kunne læse fra filen og vise det til brugeren.

## 5. Ordsky
Lav et program, der kan lave en ordsky ud fra en tekst. Programmet skal tage en tekst som input og så lave en ordsky ud fra teksten. Programmet skal kunne tage højde for, at der er forskel på store og små bogstaver. Programmet skal også kunne tage højde for, at der er forskel på ord med og uden punktum.

## 5. Lommeregner
Lav en lommeregner. Programmet skal tage to tal og en operator som input fra brugeren. Programmet skal så udføre den ønskede operation på de to tal og vise resultatet til brugeren.

## 6. Emoji oversætter
Lav et program, der kan oversætte en tekst til emojis. Programmet skal tage en tekst som input og så oversætte den til emojis. Programmet skal kunne oversætte til mindst 5 forskellige emojis.

## 7. Youtube downloader
Lav et program, der kan downloade en video fra youtube. Programmet skal tage en youtube url som input og så downloade videoen. Programmet skal også kunne downloade kun lyden fra en video.

I kan bruge biblioteket [pytube](https://python-pytube.readthedocs.io/en/latest/) til at downloade videoer fra youtube.

Herunder et eksempel:

```python
from pytube import YouTube

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
yt = YouTube(url)

# Download video

yt.streams.first().download()

# Download audio

yt.streams.filter(only_audio=True).first().download()
```

## 8. Tekstbaseret rollespil

Lav et tekstbaseret rollespil. Programmet skal tage input fra brugeren og så vise en tekst til brugeren. Programmet skal kunne håndtere, at brugeren skriver noget forkert. Programmet skal også kunne håndtere, at brugeren skriver noget, der ikke giver mening.

## 9. Lyrikmaskine

Lav et program, der kan generere lyrik. Programmet skal tage et input fra brugeren og så generere en tekst ud fra det. Programmet skal kunne generere mindst 5 forskellige tekster.

## 10. Chatbot 

Lav en chatbot. Programmet skal tage et input fra brugeren og så svare på det. Programmet skal kunne svare på mindst 5 forskellige input.

Herunder et eksempel:

```python   
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"min hobby er (.*)",
        ["Åh, jeg kan også godt lide %1"]
    ],
    [
        r"hej (.*)",
        ["Hej, hvordan har du det?"]
    ],
    [
        r"hej",
        ["Hej, hvordan har du det?"]
    ],
    [
        r"(.*) vejret (.*)",
        ["Det er dejligt vejr i dag"]
    ],
    [
        r"(.*) hedder (.*)",
        ["Mit navn er Chatbot"]
    ],
    [
        r"(.*) alder (.*)",
        ["Jeg er 100 år gammel"]
    ],
    [
        r"(.*) (kæledyr|dyr) (.*)",
        ["Jeg har en hund"]
    ],
    [
        r"quit",
        ["Farvel, det var hyggeligt at snakke med dig. Håber vi ses snart igen"]
    ],
]

def chat():
    print("Hej, jeg er en chatbot. Hvad hedder du?")

    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()
```

## 11. Tekst til tale

Lav et program, der kan læse en tekst op. Programmet skal tage en tekst som input og så læse den op. Programmet skal også kunne gemme den indtastede tekst som en lydfil.

I kan bruge biblioteket [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) til at læse tekst op.

Herunder et eksempel:

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Hej, jeg er en chatbot")
engine.runAndWait()
```

## 12. Tegneprogram

Lav et program, der kan tegne. Programmet skal kunne tegne mindst 5 forskellige figurer. Programmet skal også kunne gemme tegningen som en fil.

I kan bruge biblioteket [turtle](https://docs.python.org/3/library/turtle.html) til at tegne.

Herunder et eksempel:

```python
import turtle

t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

turtle.done()
```

## 13. Ansigtsgenkendelse

Lav et program, der kan genkende ansigter. Programmet skal tage et billede som input og så genkende ansigterne på billedet. Programmet skal også kunne genkende, om der er et bestemt ansigt på billedet.

I kan bruge biblioteket [face_recognition](https://pypi.org/project/face-recognition/) til at genkende ansigter.

Herunder et eksempel:

```python
import face_recognition

image = face_recognition.load_image_file("biden.jpg") # kræver at der er et billede i samme mappe som koden er i
face_locations = face_recognition.face_locations(image)

print(face_locations)
```

## 14. Genkend køn på billede

Lav et program, der kan genkende køn på et billede. Programmet skal tage et billede som input og så genkende kønnet på billedet. Programmet skal også kunne genkende, om der er en bestemt person på billedet.

I kan bruge biblioteket [face_recognition](https://pypi.org/project/face-recognition/) til at genkende køn.

Herunder et eksempel:

```python
import face_recognition

image = face_recognition.load_image_file("biden.jpg") # kræver at der er et billede i samme mappe som koden er i
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

print(face_encodings)
```
Her er face_encodings en liste af lister. Hver liste indeholder 128 tal. Disse tal kan bruges til at genkende ansigter, og face_locations kan bruges til at finde ud af, hvor ansigterne er på billedet.


## 15. Twitter/X bot

Lav et program, der kan poste på Twitter/X. Programmet skal tage en tekst som input og så poste den på Twitter/X. 

I kan bruge biblioteket [tweepy](https://www.tweepy.org/) til at poste på Twitter.

Herunder et eksempel:

```python
import tweepy

consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
```

## 16. Kodeordsgenerator
Lav en kodeordsgenerator. Programmet skal tage et input fra brugeren og så generere et kodeord ud fra det. Programmet skal kunne generere mindst 5 forskellige kodeord.

Udvid så programmet, så det kan gemme kodeordet i en fil.

## 17. Nyhedsscrape
Lav et program, der kan scrape nyheder fra en hjemmeside. Programmet skal tage en url som input og så scrape nyhederne fra den pågældende hjemmeside. Programmet skal også kunne gemme nyhederne i en fil.

Herunder et eksempel:
    
    ```python
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.dr.dk/nyheder/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")

    for article in articles:
        print(article.find("h3").text)
    ```
## 18. Nyhedsanalyse
Lav et program, der kan analysere nyheder. Programmet skal tage en tekst som input og så analysere den. Programmet skal kunne analysere mindst 5 forskellige tekster.

I kan bruge biblioteket [textblob](https://textblob.readthedocs.io/en/dev/) til at analysere tekster.

Herunder et eksempel:

```python
from textblob import TextBlob

text = "I love you"
blob = TextBlob(text)

print(blob.sentiment)
```

## 19. Beslutningstagning
Lav et program, der kan hjælpe med beslutningstagning. Programmet skal tage et input fra brugeren og så hjælpe med at tage en beslutning. Programmet skal kunne hjælpe med at tage mindst 5 forskellige beslutninger.

## 20. Morsekode oversætter
Lav et program, der kan oversætte til og fra morsekode. Programmet skal tage en tekst som input og så oversætte den til morsekode. Programmet skal også kunne oversætte fra morsekode til tekst.

Herunder et eksempel:
    
    ```python
    from morse import Morse

    m = Morse()

    print(m.encode("Hello World"))
    print(m.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))
    ```



