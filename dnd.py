#https://www.dnd5eapi.co/api/monsters/
import requests
import jsonpickle
import json
import sys

hd = ''

def printStats(monsterJson):
    critter = monsterJson['name']
    size = monsterJson['size']
    ac = monsterJson['armor_class']
    hd = monsterJson['hit_dice']
    avgHp = monsterJson['hit_points']
    cr = monsterJson['challenge_rating']
    #special = monsterJson['special_abilities']
    #print(special)
    #specialJson = json.load(special)
    #for each this
    specialName = monsterJson['special_abilities'][0]['name']
    specialDesc = monsterJson['special_abilities'][0]['desc']
    print('-------------------------------------')
    print(critter + " size " + size)
    print("AC " + str(ac))
    print("Hit Dice " + str(hd))
    print("Avg HP " + str(avgHp))
    print ("CR: " + str(cr))
    print("Special: " + specialName)
    print(specialDesc)
    print('-------------------------------------')
    
#print(len(sys.argv))
if len(sys.argv) < 2:
    print("Usage: --> py dnd.py monsterName")
    print("Enter the monster name")
    name = input()
elif len(sys.argv) == 2:
    name = sys.argv[1]
elif len(sys.argv) > 2:
    print("Just using " + sys.argv[1])
    name = sys.argv[1]
else:
    print("Usage: --> py dnd.py monsterName")
    print("Enter the monster name")
    name = input()

name = name.replace(" ", "-")#required for the API

#print("You entered " + name)
#url = "https://api.open5e.com/monsters/?search=" + name
url = "https://www.dnd5eapi.co/api/monsters/" + name
#print(url)
print('')
response = requests.get(url)
if response.status_code == 404:
    print(name + " not found on site")
else:
    #print(response.json())
    #json = response.json()
    #print(json)
    jsonString = response.json()
    text = json.dumps(jsonString, sort_keys=False, indent=5)
    #print(text)
    printStats(jsonString)



