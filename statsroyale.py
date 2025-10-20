import requests
from bs4 import BeautifulSoup

response = requests.get("https://cdn.statsroyale.com/gamedata-v4.json")
result_deck_popular = requests.get("https://stats-royale-api-js-beta-z2msk5bu3q-uk.a.run.app/deckbuilder/search?size=30&source=pathoflegend&sort=count")

content_html = response.text
print(response.status_code)

content_deck_popular = result_deck_popular.text

with open("all_data_CR.html", "w") as file:
    file.write(content_html)

with open("deck_popular.html", "w") as file2:
    file2.write(content_deck_popular)

# soup = BeautifulSoup(content_html, "html.parser")
soup = BeautifulSoup(content_deck_popular, "html.parser")
soup.prettify()