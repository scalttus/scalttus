import json

dictionary = {}
with open('Hama.json', 'r') as datei:
    print(dictionary)
    dictionary = json.load(datei)
    
print(dictonary[artnr])