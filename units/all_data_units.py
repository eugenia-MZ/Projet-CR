import requests
from bs4 import BeautifulSoup
import json

anti_air_troop_units = ["fire-spirit", "spear-goblins", "bats", "archers", "minions", "goblin-gang", "firecracker", "skeleton-dragons", "tesla", "minion-horde", "rascals", "ice-golem", "mega-minion", "dart-goblin", "musketeer", "goblin-hut", "flying-machine", "furnace", "zappies", "inferno-tower", "wizard", "three-musketeers", "baby-dragon", "hunter", "witch", "electro-dragon", "executioner", "goblin-giant", "princess", "ice-wizard", "electro-wizard", "inferno-dragon", "phoenix", "magic-archer", "night-witch", "mother-witch", "ram-rider", "spirit-empress", "little-prince", "archer-queen", "goblinstein"]

big_tank_units = ["royal-giant", "elixir-golem", "giant", "rune-giant", "giant-skeleton", "goblin-giant", "pekka", "electro-giant", "golem", "mega-knight", "lava-hound", "goblinstein"]

building_units = ["cannon", "mortar", "tesla", "tombstone", "goblin-cage", "goblin-hut", "bomb-tower", "inferno-tower", "barbarian-hut", "elixir-collector", "goblin-drill", "x-bow"]

mini_tank_units = ["knight", "rascals", "elite-barbarians", "ice-golem", "mini-pekka", "goblin-cage", "valkyrie", "battle-ram", "hog-rider", "battle-healer", "goblin-demolisher", "baby-dragon", "dark-prince", "prince", "bowler", "executioner", "cannon-cart", "miner", "royal-ghost", "bandit", "fisherman", "lumberjack", "ram-rider", "goblin-machine", "spirit-empress", "golden-knight", "skeleton-king", "mighty-miner", "monk", "boss-bandit"]

spell_units = ["zap", "giant-snowball", "arrows", "royal-delivery", "earthquake", "fireball", "rocket", "mirror", "barbarian-barrel", "goblin-curse", "rage", "goblin-barrel", "vines", "clone", "tornado", "void", "freeze", "poison", "lightning", "the-log", "graveyard"]

win_condition_units = ["skeleton-barrel", "mortar", "royal-giant", "elixir-golem", "battle-ram", "hog-rider", "giant", "royal-hogs", "three-musketeers", "wall-breakers", "goblin-barrel", "goblin-drill", "balloon", "goblin-giant", "x-bow", "electro-giant", "golem", "miner", "ram-rider", "graveyard", "lava-hound"]

all_units = anti_air_troop_units + big_tank_units + building_units + mini_tank_units + spell_units + win_condition_units
print(all_units)


categories = {
    "anti-air-troop": anti_air_troop_units,
    "big-tank": big_tank_units,
    "building": building_units,
    "mini-tank": mini_tank_units,
    "spell": spell_units,
    "win-condition": win_condition_units
}

# Construction de la liste de toutes les cartes
all_units = []
for cat_name, unit_list in categories.items():
    for unit in unit_list:
        all_units.append({"name": unit, "category": cat_name})

all_units_url = []

for unit in all_units:
    url_unit = f"https://www.deckshop.pro/card/detail/{unit["name"]}"
    all_units_url.append(url_unit)

print(all_units_url)

all_data_units = []

for unit_info in all_units:

    unit = unit_info["name"]
    category = unit_info["category"]

    url_unit = f"https://www.deckshop.pro/card/detail/{unit}"
    print(f"Scraping {unit} ({category})...")
    
    all_units_response = requests.get(url_unit)
    all_units_content = all_units_response.text

    soup = BeautifulSoup(all_units_content, "html.parser")
    # dictionnaire pour les stats
    data_unit = {"name": soup.find("h1").get_text(strip=True), "category": category} 
    data_unit["name"] = soup.find("h1").get_text(strip=True)

    for row in soup.find_all("tr"):
        th = row.find("th", class_="text-gray-muted font-normal")
        td = row.find("td", class_="text-right")
        
        if th and td:
            key = ''.join(th.find_all(string=True, recursive=False)).strip()
            value = td.get_text(strip=True)
            data_unit[key] = value
            
    all_data_units.append(data_unit)

    # with open("all_data_units.json", "w") as file:
    #     json.dump(all_data_units, file)

print(all_data_units)
