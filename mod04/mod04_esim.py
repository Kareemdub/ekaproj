#while-toistorakenne eli silmukka eli luuppi
import random
from operator import truediv

suorita_silmukka = True

while suorita_silmukka:
    suorita_silmukka = False
    print("totta")
    print("on")

print("Silmukan suoritus loppui")

#iteraattori ja while

toistojen_lkm = 10
i = 0
while i < toistojen_lkm:
    i = i + 1
    i += 1
    print(f"iteroiva silmukka, i:n silmukka {i}")
print(f"i:n arvo on lopuksi:{i}")

# komentokehotesovellus
app_running = True
while app_running:
    command = input("Komento> ")
    print(f"komento: {command}")
    if command == "lopeta":
        app_running = False
    elif command == "laskukone":
        luku1 = float(input("anna ensimmäinen luku: "))
        luku2 = float(input("anna toinen luku: "))
        tulos = float(luku1) + float(luku2)  #
        tulos_yhteenlasku = luku1 + luku2

        print("yhteenlaskuntoimituksen tulos: " + str(
            tulos_yhteenlasku))  # merkkijonot yhdistetään tarvitsee lukumuuttujan


#kolikonheittosimulaattori
n = 10000
i = 0
kolikko_pystyssa_lkm = 0
kruuna = 0
klaava = 0
while i < n:
    satunnaisluku = random.randint(1, 100)
    print(f"arvottu luku: {satunnaisluku}")
    if satunnaisluku < 50:
        print("Kruuna")
        kruuna += 1
    elif satunnaisluku > 50:
        print ("Klaava")
        klaava += 1
    else: # totetutuu kun arvottu luku on tasan 50 (1/101)
        print ("Kolikko pystyssä")
        kolikko_pystyssa_lkm += 1
    i = i + 1

print(f"Kolikko pystyssa: {kolikko_pystyssa_lkm}\n"
      f"Klaava: {klaava}\n"
      f"Kruuna: {kruuna}")


#noppaesimerkki 3 materiaalista
pelikerrat = 0
heittojen_lkm = 0
noppa_app_running = True
while noppa_app_running:
    noppa1 = 0
    noppa2 = 0
    heitot = 0
    while noppa1 != 6 or noppa2 != 6:
        noppa1 = random.randint(1, 6)
        noppa2 = random.randint(1, 6)
        heitot = heitot + 1

    print(f"Kahteen kutoseen tarvittiin {heitot} heittoa")
    pelikerrat += 1
    heittojen_lkm = heittojen_lkm + heitot
    komento = input("pelataanko uudestaan (k/e)?")
    if komento != "k":
        noppa_app_running = False
print(f"Kaksi kutosta saatiin keskimäärin:{heittojen_lkm / pelikerrat} heitolla.")
