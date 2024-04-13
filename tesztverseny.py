print(f'1. feladat: Az adatok beolvasása')
adatok = []

with open(f'valaszok.txt','r', encoding='utf-8') as file:
    helyes_valasz = file.readline().strip()
    for i in file:
        i = i.strip().split()
        dict = {}
        dict['id'] = i[0]
        dict['valasz'] = i[1]
        adatok.append(dict)

print(f'\n2. feladat: A vetélkedőn {len(adatok)} versenyző indult.')

print()
valasztott_azonosito = input(f'3. feladat: A versenyző azonosítója = ')
versenyzo_valasza = None
versenyzok = set()

for x in adatok:
    versenyzok.add(x['id'])
    if x['id'] == valasztott_azonosito:
        versenyzo_valasza = x['valasz']
print(f'{versenyzo_valasza}\t(a versenyző válasza)')

print(f'\n4. feladat')
print(f'{helyes_valasz}\t(a helyes megoldás)')

for x in range(len(helyes_valasz)):
    if helyes_valasz[x] == versenyzo_valasza[x]:
        print(f'+',end='')
    else:
        print(f' ',end='')

print(f'\t(a versenyző helyes válaszai)')

valasztott_feladat = int(input(f'\n5. feladat: A feladat sorszáma = '))
helyes = 0
for i in adatok:
    if i['valasz'][valasztott_feladat-1] == helyes_valasz[valasztott_feladat-1]:
        helyes += 1

print(f'A feladatra {helyes} fő, a versenyzők {round(helyes/len(adatok)*100,2)}%-a adott helyes választ.')

print(f'\n6. feladat: A versenyzők pontszámának meghatározása')
ujfile = open(f'pontok.txt','w')

pontszamlista = []

def pontoz(helyes, valasz):
    pontszam = 0
    for index in range(len(helyes)):
        if valasz[index] == helyes[index]:
            if 0 <= index <= 4:
                pontszam += 3
            elif 5 <= index <= 9:
                pontszam += 4
            elif 10 <= index <= 12:
                pontszam += 5
            elif index == 13:
                pontszam += 6
    return pontszam

for x in adatok:
    pontszamlista.append((x['id'],pontoz(helyes_valasz, x['valasz'])))
    print(x["id"], pontoz(helyes_valasz, x['valasz']),file=ujfile)

ujfile.close()

def take_second(x):
    return x[1]

pontszamlista = sorted(pontszamlista, key=take_second, reverse=True)

helyezes = 1
for index, x in enumerate(pontszamlista):
    if index < len(pontszamlista) - 1:
        if helyezes < 4:
            print(f'{helyezes}. díj ({x[1]} pont): {x[0]}')
            if pontszamlista[index+1][1] < pontszamlista[index][1]:
                helyezes += 1
            elif pontszamlista[index][1] == pontszamlista[index][1]:
                continue
        