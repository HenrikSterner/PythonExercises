import requests
from bs4 import BeautifulSoup
import random
import os
from dotenv import load_dotenv

load_dotenv()

# Henter username og password ud fra systemvariablerne
#username = os.getenv('lectiousername')
#password = os.getenv('lectiopassword')


def login(username: str, password: str):
    session = requests.Session()

    # Data til HTTP request
    data = {
        "time": 0,
        "__EVENTTARGET": "m$Content$submitbtn2",
        "__EVENTARGUMENT": "",
        '__EVENTVALIDATION': 'MM7/wLeuyH6xPMmXLgpkaRtyuqEiYLgBVc1PlCFtNzq1cFcZgyzYkJTEtNTXVM3C1n8h133MIOhxPedd6hnfY76LId9mqpTCQjoRbujNqP9Of0JQClXqugjsyunT/tAzVPXezEgc9a79GKkXrJcMbb/HLlntuYknwaqWNp74S8YCh6P1TMp8bs5Zq9OxnXlicyAFhom2/lXr+Xf0QwGaYgq6isySGPnFWDOjVLAbzOk=',
        "__SCROLLPOSITION": "",
        "__VIEWSTATEY_KEY": "",
        "__VIEWSTATE": "",
        "m$Content$username": username,
        "m$Content$password": password
    }
    # Laver login requestet
    session.post("https://www.lectio.dk/lectio/518/login.aspx", data=data)
    return session


def checkLogin(session):
    # Tjek for succesfuldt login
    r = session.get("https://www.lectio.dk/lectio/518/forside.aspx")

    if "indtaste dit brugernavn og adgangskode" in r.text:
        return "Du er ikke logget ind"
    else:
        return "Du er logget ind"


def getStudents(session):
    # Hent klassens navne
    r = session.get(
        "https://www.lectio.dk/lectio/518/subnav/members.aspx?holdelementid=44491249342&showstudents=1")
    soup = BeautifulSoup(r.content, "html.parser")

    navne = []

    for elev in range(0, 35):
        navn = soup.select_one(
            f"#s_m_Content_Content_laerereleverpanel_alm_gv_ctl{elev:02d}_lnk1")

        if navn != None:
            navne.append(navn.text)
    return navne


#session = login(username, password)
# print(checkLogin(session))

#navne = getStudents(session)

# Klasselisten
#print("Klasselisten er:")
# for navn in navne:
#    print(navn, end="\n")
# print("")

# Tager et tilfældigt navn
#print(f"Dagens heldige person er: **{random.choice(navne)}**")
