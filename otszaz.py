adatok = []
dict = {}
with open(f'penztar.txt','r',encoding='utf-8') as file:
    for x in file:
        x = x.strip()
        if x != 'F':
            if x not in dict.keys():
                dict[x] = 1
            else:
                dict[x] += 1
        else:
            adatok.append(dict)
            dict = {}

print(f'2. feladat')
print(f'A fizetések száma: {len(adatok)}')

print(f'\n3. feladat')
print(f'Az első vásárló {sum(adatok[0].values())} darab árucikket vásárolt.')

print(f'\n4. feladat')
valasztott_sorszam = 2          #int(input(f'Adja meg egy vásárlás sorszámát! '))
valasztott_arucikk = 'kefe'     #int(input(f'Adja meg egy árucikk nevét! '))
valasztott_darabszam = 2        #int(input(f'Adja meg a vásárolt darabszámot! '))

print(f'\n5. feladat')
elso = None
utolso = None
db = 0

for index, x in enumerate(adatok):
    if valasztott_arucikk in x.keys():
        db += 1
        if elso == None:
            elso = index + 1
        else:
            utolso = index + 1

print(f'Az első vásárlás sorszáma: {elso}')
print(f'Az utolsó vásárlás sorszáma: {utolso}')
print(f'{db} vásárlás során vettek belőle.')

print(f'\n6. feladat')
def ertek(db):
    if db == 1:
        ertek = 500
    elif db == 2:
        ertek = 950
    elif db == 3:
        ertek = 1350
    elif db >= 4:
        ertek = 1350 + 400*(db-3)
    return ertek

print(f'{valasztott_darabszam} darab vételekor fizetendő: {ertek(valasztott_darabszam)}')

print(f'\n7. feladat')
for x in adatok[valasztott_darabszam-1].items():
    print(x[0], x[1], sep=' ')

#8. feladat
ujfile = open(f'osszeg.txt','w')
for index, x in enumerate(adatok):
    print(f'{index+1}: {sum(map(ertek, adatok[index].values()))}', file=ujfile)
ujfile.close()

