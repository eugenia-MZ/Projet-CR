import requests
from bs4 import BeautifulSoup
import json

# Ouvre le fichier HTML sauvegardé
with open("Stats_Royale_english.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

units_data = []

rows = soup.find_all("tr")

for row in rows:
    # Nom de la carte
    name_tag = row.find("div", class_="text-left hidden sm:block")
    if not name_tag:
        continue

    # Met le nom tout en minuscule et remplace les espaces par des tirets
    name = name_tag.text.strip().lower().replace(" ", "-")

    # Taux de réussite et d'utilisation
    rates = row.find_all("div", class_="flex justify-end items-center text-3xl font-bold")
    if len(rates) >= 2:
        win_rate = rates[0].text.strip()
        use_rate = rates[1].text.strip()
    else:
        win_rate = use_rate = "N/A"

    # On garde uniquement si les taux existent
    if win_rate and use_rate and win_rate != "N/A":
        units_data.append({
            "name": name,
            "win_rate": win_rate,
            "use_rate": use_rate
        })

# Affiche le résultat final
print(units_data)
with open("rate_use_data.json", "w") as file:
    json.dump(units_data, file)
