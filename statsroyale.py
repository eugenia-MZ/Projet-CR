import requests
from bs4 import BeautifulSoup

response = requests.get("https://statsroyale.com/fr/deckbuilder")

content_html = response.text
print(response.status_code)

with open("result_scrap.html", "w") as file:
    file.write(content_html)

soup = BeautifulSoup(content_html, "html.parser")