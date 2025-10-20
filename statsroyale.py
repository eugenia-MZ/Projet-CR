import requests
from bs4 import BeautifulSoup

categories = ["anti-air-troop", "big-tank", "mini-tank", "building", "spell"]
all_categories = []

for category in categories:
    url = f"https://www.deckshop.pro/card/property/{category}"
    all_categories.append(url)

# print(all_categories[0])

win_condition_response = requests.get("https://www.deckshop.pro/card/flag/win-condition")

win_condition_html = win_condition_response.text

with open("win-condition.html", "w") as file:
    file.write(win_condition_html)


for url in all_categories:
    category_response = requests.get(url)
    category_content = category_response.text

    filename = url.split("/")[-1]

    with open(f"{filename}.html", "w") as file:
        file.write(category_content)

    soup_anti_air_troop = BeautifulSoup(category_content, "html.parser")