adatok = []
with open(f'tavirathu13.txt','r',encoding='utf-8') as file:
    for i in file:
        i = i.strip().split()
        dict = {}
        dict['varos'] = i[0]
        dict['ido'] = i[1]
        dict['ora'] = int(i[1][:2])
        dict['perc'] = int(i[1][2:])
        dict['szel'] = i[2]
        dict['szelirany'] = i[2][:3]
        dict['szelerosseg'] = int(i[2][3:])
        dict['hom'] = int(i[3])
        adatok.append(dict)

print(f'2. feladat')
valasztott_varos = 'SM'     #input(f'Adja meg egy település kódját! Település: ')

for x in reversed(adatok):
    if x['varos'] == valasztott_varos:
        print(f'Az utolsó mérési adat a megadott településről {x["ora"]}:{x["perc"]}-kor érkezett.')
        break

print(f'3. feladat')
legalacsonyabb_hom = 999
legmagasabb_hom = -999

legmagasabb_adat = None
legalacsonyabb_adat = None
varosok = set()
for x in adatok:
    varosok.add(x['varos'])
    if x['hom'] < legalacsonyabb_hom:
        legalacsonyabb_hom = x['hom']
        legalacsonyabb_adat = x
    elif x['hom'] > legmagasabb_hom:
        legmagasabb_hom = x['hom']
        legmagasabb_adat = x

print(f'A legalacsonyabb hőmérséklet: {legalacsonyabb_adat["varos"]} {legalacsonyabb_adat["ora"]}:{legalacsonyabb_adat["perc"]} {legalacsonyabb_adat["hom"]} fok. ')
print(f'A legalacsonyabb hőmérséklet: {legmagasabb_adat["varos"]} {legmagasabb_adat["ora"]}:{legmagasabb_adat["perc"]} {legmagasabb_adat["hom"]} fok. ')

print(f'4. feladat')
volt_ilyen = False
for x in varosok:
    idopont = None
    for y in adatok:
        if y['varos'] == x:
            if y['szel'] == '00000':
                    volt_ilyen = True
                    print(f'{x} {y["ido"][:2]}:{y["ido"][2:]}')

if not volt_ilyen:
    print('Nem volt szélcsend a mérések idején.')

print(f'5. feladat')
for x in varosok:
    egy = False
    het = False
    tizenharom = False
    tizenkilenc = False
    kozepho = 0
    szamlalo = 0
    min_hom = 999
    max_hom = -999
    for y in adatok:
        if y['varos'] == x:
            if y['ora'] == 1:
                egy = True 
                szamlalo += 1
                kozepho += y['hom']
            
            if y['ora'] == 7:
                het = True 
                szamlalo += 1
                kozepho += y['hom']
            
            if y['ora'] == 13:
                tizenharom = True 
                szamlalo += 1
                kozepho += y['hom']
            
            if y['ora'] == 19:
                tizenkilenc = True 
                szamlalo += 1
                kozepho += y['hom']
            
            if min_hom > y['hom']:
                min_hom = y['hom']
            
            if max_hom < y['hom']:
                max_hom = y['hom']
    
    if egy and het and tizenharom and tizenkilenc:
        print(f'{x} Középhőmérséklet: {int(round(kozepho/szamlalo,0))}; Hőmérséklet-ingadozás: {max_hom-min_hom}')
            
    else:
        print(f'{x} Középhőmérséklet: NA; Hőmérséklet-ingadozás: {max_hom-min_hom}')

#6. feladat
for x in varosok:
    ujfile = open(f'{x}.txt','w')
    print(f'{x}', file=ujfile)
    for y in adatok:
        if y['varos'] == x:
            print(f'{y["ido"][:2]}:{y["ido"][2:]} {y["szelerosseg"]*"#"}',file=ujfile)
    ujfile.close()

    

                
