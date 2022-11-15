import json

def resolve_id(name):
    name = name.lower()
    name = name.replace(' ', '-')
    with open("locations.json") as locations:
        locations = json.load(locations)
        if name in locations:
            return locations[name]
        else: return None

