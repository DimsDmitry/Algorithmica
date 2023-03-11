import json


weather = {}


with open('weather.json', 'w', encoding='UTF-8') as file:
    json.dump(weather, file, ensure_ascii=False)

with open('weather.json', 'r') as file:
    weather = json.load(file)


print(weather)
