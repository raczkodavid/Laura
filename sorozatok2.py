adatok = []
dict = {}
with open(f'lista.txt','r', encoding='utf-8') as file:
    for x in file:
        x = x.strip()
        dict['datum'] = x
        dict['angol'] = next(file)
        dict['evadepi'] = next(file)
        dict['hossz'] = int(next(file))
        dict['latta'] = int(next(file))
        adatok.append(dict)
        dict = {}

print(f'2. feladat')
print(f'A listában {len(adatok) - len([x["datum"] for x in adatok if x["datum"] == "NI"])} db vetítési dátummal rendelkező epizód van.')

print(f'\n3. feladat')
latta = len([x["datum"] for x in adatok if x["latta"] == 1])
print(f'A listában lévő epizódok {round(latta / len(adatok) * 100, 2)}%-át látta.')

print(f'\n4. feladat')
sorozat_percek = sum([x["hossz"] for x in adatok if x["latta"] == 1])
print(f'Sorozatnézéssel {sorozat_percek // 1440} napot {sorozat_percek % 1440 // 60} órát és {sorozat_percek % 60} percet töltött.')

print(f'\n5. feladat')
bekert_datum = input(f'Adjon meg egy dátumot! Dátum= ')
for x in adatok:
    if x['datum'] <= bekert_datum:
        if x['latta'] == 0:
            print(f'{x["evadepi"]}\t{x["angol"]}')

#6. feladat
def hetnapja(ev, ho, nap):
    napok = ('v', 'h', 'k', 'sze', 'cs', 'p', 'szo')
    honapok = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    if ho < 3:
        ev = ev -1
    return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]

print(f'\n7. feladat')
bekert_nap = input(f'Adja meg a hét egy napját (például cs)! Nap= ')
print(set(x["angol"] for x in adatok if x["datum"] != 'NI' and hetnapja(int(x["datum"][:4]), int(x["datum"][5:7]), int(x["datum"][8:])) == bekert_nap),sep='\n')

#8. feladat
ujfile = open(f'summa.txt', 'w')
sorozatok = set(x["angol"] for x in adatok)
for x in sorozatok:
    vetitesi_ido = 0
    episzam = 0
    for y in adatok:
        if y['angol'] == x:
            vetitesi_ido += y['hossz']
            episzam += 1
    print(x, vetitesi_ido, episzam, sep=' ', file=ujfile)
ujfile.close()


