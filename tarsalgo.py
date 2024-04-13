adatok = []
with open(f'ajto.txt', 'r', encoding='utf-8') as file:
    for x in file:
        x = x.strip().split()
        for y in range(3):
            x[y] = int(x[y])
        dict = {}
        dict['ora'] = x[0]
        dict['perc'] = x[1]
        if x[1] < 10:
            dict['ido'] = f'{x[0]}:0{x[1]}'
        else:
            dict['ido'] = f'{x[0]}:{x[1]}'
        dict['id'] = x[2]
        dict['ajto'] = x[3]
        adatok.append(dict)

print(f'2. feladat')
elso_belepo = [x['id'] for x in adatok if x['ajto'] == 'be'][0]
utolso_kilepo = [x['id'] for x in adatok if x['ajto'] == 'ki'][-1]

print(f'Az első belépő: {elso_belepo}')
print(f'Az utolsó kilépő: {utolso_kilepo}')

#3. feladat
ujfile = open(f'athaladasok.txt','w')
szemelyek = set(x['id'] for x in adatok)
for x in szemelyek:
    athaladasok_szama = 0
    for y in adatok:
        if y['id'] == x:
            athaladasok_szama += 1
    print(x, athaladasok_szama, sep=' ', file=ujfile)
ujfile.close()

print(f'\n4. feladat')
tarsalgoban = []
for x in adatok:
    if x['ajto'] == 'be':
        tarsalgoban.append(x['id'])
    elif x['ajto'] == 'ki' and x['id'] in tarsalgoban:
        tarsalgoban.remove(x['id'])

print(f'A végén a társalgóban voltak: {" ".join(map(str, sorted(tarsalgoban)))}')

print(f'\n5. feladat')
max_tarsalgoban = 0
jelenleg_tarsalgoban = 0
max_idopont = None

for x in adatok:
    if x['ajto'] == 'be':
        jelenleg_tarsalgoban += 1
        if jelenleg_tarsalgoban > max_tarsalgoban:
            max_tarsalgoban = jelenleg_tarsalgoban
            max_idopont = x['ido']
    
    elif x['ajto'] == 'ki':
        jelenleg_tarsalgoban -= 1

print(f'Például {max_idopont}-kor voltak a legtöbben a társalgóban.')

print(f'\n6. feladat')
bekert_szemely = int(input(f'Adja meg a személy azonosítóját! '))

print(f'\n7. feladat')
eltoltott_ido = 0
for x in adatok:
    if x['id'] == bekert_szemely:
        if x['ajto'] == 'be':
            be = x
        elif x['ajto'] == 'ki':
            ki = x
            print(f'{be["ido"]}-{ki["ido"]}')
            eltoltott_ido += ((int(ki["ora"])*60+int(ki["perc"]))-(int(be["ora"])*60+int(be["perc"])))
            be = None

if bekert_szemely in tarsalgoban:
    print(f'{be["ido"]}-')
    eltoltott_ido += 15*60 - be["ora"]*60 - be["perc"]
    print(f'\n8. feladat')
    print(f'A(z) {bekert_szemely}. személy összesen {eltoltott_ido} percet volt bent, a megfigyelés végén a társalgóban volt.')

else:
    print(f'\n8. feladat')
    print(f'A(z) {bekert_szemely}. személy összesen {eltoltott_ido} percet volt bent, a megfigyelés végén nem volt a társalgóban.')




