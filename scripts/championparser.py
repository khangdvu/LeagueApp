from champions.models import Champion
import json

with open('res/champion.json', encoding="utf8") as inputFile:
    data = json.load(inputFile)
    champions = data['data']
    for key,currentChamp in champions.items():
        entry = Champion(
        name=currentChamp['name'],
        hp=currentChamp['stats']['hp'],
        hpperlevel = currentChamp['stats']['hpperlevel'],
        mp = currentChamp['stats']['mp'],
        mpperlevel = currentChamp['stats']['mpperlevel'],
        movespeed = currentChamp['stats']['movespeed'],
        armor = currentChamp['stats']['armor'],
        armorperlevel = currentChamp['stats']['armorperlevel'],
        spellblock = currentChamp['stats']['spellblock'],
        spellblockperlevel = currentChamp['stats']['spellblockperlevel'],
        attackrange = currentChamp['stats']['attackrange'],
        hpregen = currentChamp['stats']['hpregen'],
        hpregenperlevel = currentChamp['stats']['hpregenperlevel'],
        mpregen = currentChamp['stats']['mpregen'],
        mpregenperlevel = currentChamp['stats']['mpregenperlevel'],
        crit = currentChamp['stats']['crit'],
        critperlevel = currentChamp['stats']['critperlevel'],
        attackdamage = currentChamp['stats']['attackdamage'],
        attackdamageperlevel = currentChamp['stats']['attackdamageperlevel'],
        attackspeedperlevel = currentChamp['stats']['attackspeedperlevel'],
        attackspeed = currentChamp['stats']['attackspeed']
        )
        entry.save()
