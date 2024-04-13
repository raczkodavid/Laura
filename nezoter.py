#1. feladat
f1 = open(f'foglaltsag.txt', 'r') 
foglaltsag = []
for i in f1:
    i = i.strip()
    foglaltsag.append(i)
f1.close()

f2 = open(f'kategoria.txt', 'r')
kategoriak = []
for i in f2:
    i = i.strip()
    kategoriak.append(i)
f2.close()

#2. feladat
print(f'2. feladat')
bekert_sor = int(input(f'Adjon meg egy sorszámot! '))
bekert_oszlop = int(input(f'Adjon meg egy oszlop sorszámot! '))

if foglaltsag[bekert_sor-1][bekert_oszlop-1] == 'x':
    print(f'A hely már foglalt!')
else:
    print(f'A hely még szabad!')

#3. feladat
osszes_hely = len(foglaltsag[0]) * len(foglaltsag)
foglalt = 0
for x in foglaltsag:
    foglalt += x.count('x')

print(f'Az előadásra eddig {foglalt} jegyet adtak el, ez a nézőtér {round(foglalt/osszes_hely*100)}%-a.')

#4. feladat
elso = 0
masodik = 0
harmadik = 0
negyedik = 0
otodik = 0

for index1, x in enumerate(foglaltsag):
    for index2, y in enumerate(x):
        if y == 'x':
            if kategoriak[index1][index2] == '1':
                elso += 1
            elif kategoriak[index1][index2] == '2':
                masodik += 1
            elif kategoriak[index1][index2] == '3':
                harmadik += 1
            elif kategoriak[index1][index2] == '4':
                negyedik += 1
            elif kategoriak[index1][index2] == '5':
                otodik += 1

kat = [elso, masodik, harmadik, negyedik, otodik]
kat_max = max(kat)
kat_index_max = None

for index, i in enumerate(kat):
    if i == kat_max:
        kat_index_max = index

print(f'A legtöbb jegyet a(z) {kat_index_max+1}. árkategóriában értékesítették.')

#5. feladat
bevetel = elso * 5000 + masodik * 4000 + harmadik * 3000 + negyedik * 2000 + otodik * 1500
print(f'A színház pillanatnyi bevétele: {bevetel}Ft.')

#6. feladat
egyedulallo_ures_helyek = 0
for i in foglaltsag:
    for index, x in enumerate(i):
        if 0 < index < len(i) - 1:
            if i[index-1] == 'x' and i[index] == 'o' and i[index+1] == 'x':
                egyedulallo_ures_helyek += 1

    if i[-1] == 'o' and i[-2] == 'x':
        egyedulallo_ures_helyek += 1
    
    if i[0] == 'o' and i[1] == 'x':
        egyedulallo_ures_helyek += 1

print(f'Egyedülálló üres helyek száma: {egyedulallo_ures_helyek}')

f3 = open(f'szabad.txt', 'w')
szabad = []
sor = []
for index, x in enumerate(foglaltsag):
    for index1, i in enumerate(x):
        if len(sor) < 20:
            if foglaltsag[index][index1] == 'x':
                sor.append('x')
            else:
                sor.append(kategoriak[index][index1])
        if len(sor) == 20:
            szabad.append(sor)
            sor = []

for x in szabad:
    print(''.join(x), file=f3)

f3.close()
        






