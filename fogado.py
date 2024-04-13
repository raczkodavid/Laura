adatok = []
with open(f'fogado.txt','r', encoding='utf-8') as file:
    for x in file:
        x = x.strip().split()
        dict = {}
        dict['tanar'] = f'{x[0]} {x[1]}'
        dict['idopont'] = x[2]
        dict['idopontpercben'] = int(x[2][:2])*60 + int(x[2][3:])
        dict['rogzitve'] = x[3]
        adatok.append(dict)

print(f'2. feladat ')
print(f'Foglalások száma:  {len(adatok)}')

print(f'\n3. feladat')
bekert_tanar = input(f'Adjon meg egy nevet: ')
szamlalo = 0
for x in adatok:
    if x['tanar'] == bekert_tanar:
        szamlalo += 1
print(f'{bekert_tanar} néven {szamlalo} időpontfoglalás van.')

print(f'\n4. feladat')
bekert_idopont = input(f'Adjon meg egy érvényes időpontot (pl. 17:10): ')
ujfile = open(f'{bekert_idopont[:2]}{bekert_idopont[3:]}.txt','w')
foglalt = sorted(set(x['tanar'] for x in adatok if x['idopont'] == bekert_idopont))
for x in foglalt:
    print(x, file=ujfile)
ujfile.close()

print(f'\n5. feladat')
seged = [x['rogzitve'] for x in adatok]
leghamarabb = seged.index(min(seged))
print(f'Tanár neve: {adatok[leghamarabb]["tanar"]} ')
print(f'Foglalt időpont: {adatok[leghamarabb]["idopont"]}')
print(f'Foglalás ideje: {adatok[leghamarabb]["rogzitve"]}')

print(f'\n6. feladat')
def vissza_idobe(p):
    ora = p // 60
    perc = p % 60
    if perc < 10:
        perc = f'0{perc}'
    return f'{ora}:{perc}'

lehetseges_idopontok = [x for x in range(960, 1080, 10)]
foglalt_idopontok = []
for x in adatok:
    if x['tanar'] == 'Barna Eszter':
        if x['idopontpercben'] in lehetseges_idopontok:
            lehetseges_idopontok.remove(x['idopontpercben'])
            foglalt_idopontok.append(x['idopontpercben'])

print(f'Barna Eszter legkorábban távozhat: {vissza_idobe(max(foglalt_idopontok)+10)}')

