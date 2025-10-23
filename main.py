import requests
from bs4 import BeautifulSoup
import json

categories = ["anti-air-troop", "big-tank", "mini-tank", "building", "spell", "win-condition"]
all_url_categories = []

for category in categories:
    if category == "win-condition":
        all_url_categories.append("https://www.deckshop.pro/card/flag/win-condition")
    else:
        url_category = f"https://www.deckshop.pro/card/property/{category}"
        all_url_categories.append(url_category)

# print(all_url_categories[0])

win_condition_response = requests.get("https://www.deckshop.pro/card/flag/win-condition")

win_condition_html = win_condition_response.text

"""
with open("win-condition.html", "w") as file:
    file.write(win_condition_html)
"""

for url in all_url_categories:
    category_response = requests.get(url)
    category_content = category_response.text

    filename = url.split("/")[-1]

    """
    with open(f"{filename}.html", "w") as file:
        file.write(category_content)
    """

    soup = BeautifulSoup(category_content, "html.parser")

    links_units = []
    anti_air_troop_units = []

    for img in soup.find_all("img", class_="card"):
        if "opacity-30" in img.get("class", []) or "grayscale" in img.get("class", []):
            continue

        parent_a = img.find_parent("a", href=True)

        if parent_a:
            links_units.append(parent_a['href'])

    # print(f"\nFichier : {filename}")
    # print("\n".join(links_units))

    all_units = [link[13:] for link in links_units]

    # print(f"\nFichier : {filename}")
    print("\n", all_units)

    all_url_units = []

    for unit in links_units:
        url_unit = f"https://www.deckshop.pro{unit}"
        all_url_units.append(url_unit)

    print(all_url_units)

    # with open(f"units/{filename}.py", "w") as file:
    #     json.dump(all_units, file)