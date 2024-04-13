def ki(sorszam):
    print(f'{sorszam}. feladat')

#1. feladat
ki(1)
bemeneti_file_neve = 'konnyu.txt'   #input(f'Adja meg a bemeneti fájl nevét! ')
tarolt_adatok = []
bekert_sorszam = 1                  #int(input(f'Adja meg egy sor számát! '))
bekert_oszlopszam = 1                #int(input(f'Adja meg egy oszlop számát! '))

#2. feladat
with open(f'{bemeneti_file_neve}', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.strip().split()
        for x in range(len(i)):
            i[x] = int(i[x])
        tarolt_adatok.append(i)

tarolt_adatok = tarolt_adatok[:9]
#3. feladat
ki(3)
def melyik_resztabla(sor, oszlop):
    if 0 <= sor <= 3:
        if 0 <= oszlop <= 3:
            return 1
        elif 4 <= oszlop <= 6:
            return 2
        elif 7 <= oszlop <= 9:
            return 3
    
    elif 4 <= sor <= 6:
        if 0 <= oszlop <= 3:
            return 4
        elif 4 <= oszlop <= 6:
            return 5
        elif 7 <= oszlop <= 9:
            return 6
    
    elif 0 <= sor <= 3:
        if 0 <= oszlop <= 3:
            return 7
        elif 4 <= oszlop <= 6:
            return 8
        elif 7 <= oszlop <= 9:
            return 9
print(f'Az adott helyen szereplő szám: {tarolt_adatok[bekert_sorszam-1][bekert_oszlopszam-1]}')
print(f'A hely a(z) {melyik_resztabla(bekert_sorszam, bekert_oszlopszam)} résztáblázathoz tartozik.')

#4. feladat
ki(4)
kitoltetlen = 0
osszes = 0
for i in tarolt_adatok:
    kitoltetlen += i.count(0)
    osszes += len(i)

print(osszes)

print(f'Az üres helyek aránya: {round(kitoltetlen*100/osszes,1)}%')

#5. feladat
ki(5)
uj_kivalasztott_sor = 3
uj_kivalasztott_oszlop = 6
kivalasztott_szam = 7

def resztabla_masik(tabla):
    if tabla == 1:
        sor = [0, 1, 2]
        oszlop = [0, 1, 2]
    
    elif tabla == 2:
        sor = [0, 1, 2]
        oszlop = [3, 4, 5]
    
    elif tabla == 3:
        sor = [0, 1, 2]
        oszlop = [6, 7, 8]
    
    elif tabla == 4:
        sor = [3, 4, 5]
        oszlop = [0, 1, 2]
    
    elif tabla == 5:
        sor = [3, 4, 5]
        oszlop = [3, 4, 5]
    
    elif tabla == 6:
        sor = [3, 4, 5]
        oszlop = [6, 7, 8]
    
    elif tabla == 7:
        sor = [6, 7, 8]
        oszlop = [0, 1, 2]
    
    elif tabla == 8:
        sor = [6, 7, 8]
        oszlop = [3, 4, 5]
    
    elif tabla == 9:
        sor = [6, 7, 8]
        oszlop = [6, 7, 8]
    
    return sor, oszlop
    

if tarolt_adatok[uj_kivalasztott_sor-1][uj_kivalasztott_oszlop-1] != 0:
    print(f'A helyet már kitöltötték!')

else:
    #sor vizsgálat
    if kivalasztott_szam in tarolt_adatok[uj_kivalasztott_sor-1]:
        print(f'Az adott sorban már szerepel a szám!')
    
    #oszlop vizsgálat
    oszlopban_szerepel = False
    for x in tarolt_adatok:
        if x[uj_kivalasztott_oszlop-1] == kivalasztott_szam:
            oszlopban_szerepel = True
    
    if oszlopban_szerepel:
        print(f'Az adott oszlopban már szerepel a szám!')
    
    #résztábla vizsgálat
    valasztott_resztabla = melyik_resztabla(uj_kivalasztott_sor-1, uj_kivalasztott_oszlop-1)
    resztablaba_van = False
    for i in range(resztabla_masik(valasztott_resztabla)[0][0],resztabla_masik(valasztott_resztabla)[0][-1]+1):
        for x in range(resztabla_masik(valasztott_resztabla)[1][0],resztabla_masik(valasztott_resztabla)[1][-1]+1):
            if tarolt_adatok[i][x] == kivalasztott_szam:
                resztablaba_van = True
    
    if resztablaba_van:
        print(f'A résztáblázatban már szerepel a szám.')
    
    else:
        print(f'A lépés megtehető')




    
    

        





