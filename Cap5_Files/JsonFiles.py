import json

# Read a json
with open("sample.json", "r") as jsonFile:
    dic = json.load(jsonFile)
    for key, values in dic.items():
        print(key + ": " + str(values))

# Write a json
dic = {
  "CHAVES": ["CHAVES DO 8", "14/04/2017", "RECEP_01"],
  "QUICO": ["QUICO FLORES", "24/04/2017", "RAIOX_01"],
  "FLORINDA": ["DONA FLORINDA", "18/04/2017", "RECEP_03"]
}

with open("sample02.json", "w") as jsonFile:
    json.dump(dic, jsonFile)