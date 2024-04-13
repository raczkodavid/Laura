from math import sqrt
#1. feladat
def mpbe(ora, perc, masodperc):
    return ora*3600 + perc*60 + masodperc

def vissza_idobe(masodperc):
    ora = masodperc // 3600
    perc = masodperc % 3600 // 60
    mp = masodperc % 60
    return f'{ora}:{perc}:{mp}'

adatok = []
with open(f'jel.txt', 'r') as file:
    for i in file:
        szotar = {}
        i = i.strip().split()
        szotar['ido'] = mpbe(int(i[0]), int(i[1]), int(i[2]))
        szotar['x'] = int(i[3])
        szotar['y'] = int(i[4])
        adatok.append(szotar)

print('2. feladat')
valasztott_sorszam = 3#int(input(f'Adja meg a jel sorszámát! '))
print(f'x={adatok[valasztott_sorszam-1]["x"]} y={adatok[valasztott_sorszam-1]["y"]}')

#3. feladat
def eltelt(ido1, ido2):
    return ido2 - ido1

print(f'4. feladat')
print(f'Időtartam: {vissza_idobe(eltelt(adatok[0]["ido"],adatok[-1]["ido"]))}')

print(f'5. feladat')
min_x = 10000
min_y = 10000
max_x = -10000
max_y = -10000

for index, x in enumerate(adatok):
    if adatok[index]["x"] < min_x:
        min_x = adatok[index]["x"]
    elif adatok[index]["y"] < min_y:
        min_y = adatok[index]["y"]
    
    if adatok[index]["x"] > max_x:
        max_x = adatok[index]["x"]
    if adatok[index]["y"] > max_y:
        max_y = adatok[index]["y"]

print(f'Bal alsó: {min_x} {min_y}, jobb felső: {max_x} {max_y}')

print('6. feladat')
megtett_tavolsag = 0

for index, i in enumerate(adatok):
    if index < len(adatok) - 1:
        megtett_tavolsag += sqrt((adatok[index]["x"]-adatok[index+1]["x"])**2 + (adatok[index]["y"]-adatok[index+1]["y"])**2)

print(f'Elmozdulás: {round(megtett_tavolsag,3)} egység.')

ujfile = open(f'kimaradt.txt', 'w')
for index, i in enumerate(adatok):
    kord_elteres = 0
    ido_elteres = 0

    x_elteres = 0
    y_elteres = 0
    
    if index < len(adatok) - 1:
        if adatok[index+1]['ido'] - adatok[index]['ido'] > 300:
            ido_elteres = (adatok[index+1]['ido'] - adatok[index]['ido']) // 300 - 1
        
        if abs(adatok[index+1]['x'] - adatok[index]['x']) > 10 or abs(adatok[index+1]['y'] - adatok[index]['y']) > 10:
            x_elteres = abs(adatok[index+1]["x"] - adatok[index]["x"]) // 10 - 1 
            y_elteres = abs(adatok[index+1]["y"] - adatok[index]["y"]) // 10 - 1
            kord_elteres = max(x_elteres, y_elteres)
               
        if kord_elteres != 0 or ido_elteres != 0:
            if kord_elteres > ido_elteres: 
                print(f'{vissza_idobe(adatok[index+1]["ido"])} koordináta-eltérés: {kord_elteres}', file=ujfile)
            elif kord_elteres < ido_elteres:
                print(f'{vissza_idobe(adatok[index+1]["ido"])} időeltérés: {ido_elteres}', file=ujfile)
            else:
                print(f'{vissza_idobe(adatok[index+1]["ido"])} koordináta-eltérés: {kord_elteres}', file=ujfile)

ujfile.close()
    
        
    
    