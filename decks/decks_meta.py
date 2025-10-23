import requests
from bs4 import BeautifulSoup
import json

url_deck_meta = "https://www.deckshop.pro/best-decks/for/new-meta"
url_deck_meta_response = requests.get(url_deck_meta)
soup = BeautifulSoup(url_deck_meta_response.text, "html.parser")

deck_meta_data = []

decks = soup.find_all("div", class_="deck-container-wide")

for deck in decks:
    deck_alt = [img["alt"].strip().lower().replace(" ", "-") for img in deck.find_all("img", alt=True)]
    deck_meta_data.append(deck_alt)

for deck in deck_meta_data:
    print(deck)