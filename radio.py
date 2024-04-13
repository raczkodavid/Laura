#1. feladat
lista = []
counter = 0
with open(f'veetel.txt', 'r', encoding='utf-8') as file:
    for i in file:
        dict = {}
        if counter % 2 == 0:
            i = i.strip().split()
            napsorszam = int(i[0])
            amator = int(i[1])
        else:
            dict['nap'] = napsorszam
            dict['amator'] = amator
            dict['uzenet'] = i
            lista.append(dict)
        counter += 1

print(f'2. feladat')
print(f'Az első üzenet rögzítője: {lista[0]["amator"]}')
print(f'Az utolsó üzenet rögzítője: {lista[-1]["amator"]}')

print(f'\n3. feladat')
for x in lista:
    if 'farkas' in x["uzenet"]:
        print(f'{x["nap"]}. nap {x["amator"]}. rádióamatőr')

print(f'\n4. feladat')
napok = [int(x) for x in range(1, 12)]
for x in napok:
    szam = 0
    for y in lista:
        if x == y['nap']:
            szam += 1
    print(f'{x}. nap: {szam} rádióamatőr')

#5. feladat
ujfile = open('aadas.txt','w')
for x in napok:
    uzi = ['#' for i in range(91)]
    for y in lista:
        if y['nap'] == x:
            for index, z in enumerate(y['uzenet']):
                if y['uzenet'][index] != '#':
                    uzi[index] = y['uzenet'][index]
    print(''.join(uzi), file=ujfile, end='')

ujfile.close()

#6. feladat
def szame(szo):
    valasz = True
    for i in range(1, len(szo)):
        if szo[i] < '0' or szo[i] > '9':
            valasz = False
    return valasz
 
print(f'7. feladat')
valasztott_nap = 5      #int(input(f'Adja meg a nap sorszámát! '))
valasztott_amator = 18  #int(input(f'Adja meg a rádióamatőr sorszámát! '))
valasztott_uzenet = None
megallapithato = True

for x in lista:
    if x['nap'] == valasztott_nap and x['amator'] == valasztott_amator:
        valasztott_uzenet = x['uzenet']
        break

if valasztott_uzenet == None:
    print(f'Nincs ilyen feljegyzés')
else:
    elso_szokoz = valasztott_uzenet.find(' ')
    perjel = valasztott_uzenet.find('/')
    if '#' not in valasztott_uzenet[0:elso_szokoz] and szame(valasztott_uzenet[0:elso_szokoz]):
        egyedek_szama = int(valasztott_uzenet[0:perjel]) + int(valasztott_uzenet[perjel+1:elso_szokoz])
        print(f'A megfigyelt egyedek száma: {egyedek_szama}')
    else:
        print(f'Nincs információ')

print(szame('a'))



