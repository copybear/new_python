import requests
from bs4 import BeautifulSoup

def printWeb():
    url = "https://techplay.jp/column/601"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1").text
    print(title)
