import random
geheimnis = random.randint(1,10)
versuch = 0

while versuch != geheimnis:
    versuch = int(input("Rate: "))
    if versuch == 0:
        print("Das Spiel wird beendet!")
        break
    elif versuch == geheimnis:
        print("Super, du hast es geschafft!")
    elif versuch < geheimnis:
        print("Die Zahl ist zu klein")
    elif versuch > geheimnis:
        print("die Zahl ist zu groß!")
