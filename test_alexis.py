import requests
from bs4 import BeautifulSoup

cards_data = []


for link in card_links:
    print(f"\n🔗 Scraping : {link}")
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")


    # --- Nom de la carte ---
    name_tag = soup.find("h1")
    name = name_tag.text.strip() if name_tag else "Nom inconnu"


    # --- Rareté ---
    rarity_tag = soup.find("span", class_="text-teal-500")
    if not rarity_tag:  # certaines cartes ont une structure différente
        rarity_tag = soup.find("span", string=lambda t: t and t in ["Common", "Rare", "Epic", "Legendary", "Champion"])
    rarity = rarity_tag.text.strip() if rarity_tag else "Non spécifiée"


    # --- Statistiques (niveau 11 = première ligne des tableaux) ---
    stats = {}
    for row in soup.find_all("tr"):
        th = row.find("th", class_="text-gray-muted font-normal")
        td = row.find("td", class_="text-right")
        if th and td:
            stat_name = th.text.strip()
            value = td.text.strip()
            stats[stat_name] = value


    card_info = {"name": name, "rarity": rarity, **stats}
    cards_data.append(card_info)


print("✅ Scraping terminé !")
for c in cards_data:
    print(c)
