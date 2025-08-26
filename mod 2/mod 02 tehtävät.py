#tehtävä 1


nimi = input("Anna nimesi:") # pyydetään käyttäjän nimi
print (f"Terve, {nimi}!") # tervehditään käyttäjää

#tehtävä 2

import math # lisätään pi ohjelmaan

sade = float(input("Syötä ympyrän säde: ")) #pyydetään säde käyttäjältä
ympyran_pinta_ala = math.pi * sade ** 2 # pinta-ala lasku
print(f"Ympyrän pinta-ala on: {ympyran_pinta_ala:.5f}") # tulostetaan pinta-ala viiden desimaalin tarkkudella


#tehtävä 3
#kysytään suorakulmion tiedot
kanta = float(input("Syötä suorakulmion kanta: "))
korkeus = float(input("Syötä suorakulmion korkeus "))
#laskutoimitukset piiriin ja pinta-alaan
piiri = kanta * 2 + korkeus * 2
pinta_ala = kanta * korkeus
#printataan tulokset kahden desimaalin tarkkuudella.
print(f"Suorakulmion pinta-ala on {pinta_ala:.2f}"
      f"\nSuorakulmion piiri on {piiri:.2f}")


#tehtävä 4
#pyydetään käyttäjältä kolme kokonaislukua
luku1 = int(input("Syötä ensimmäinen kokonaisluku: "))
luku2 = int(input("Syötä toinen kokonaisluku: "))
luku3 = int(input("Syötä kolmas kokonaisluku: "))

#asetetaan muuttujille luvuista arvot
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

#printataan lukujen vastaukset
print("Lukujen summa on: " + str(summa))
print("Lukujen tulo on: " + str(tulo))
print("Lukujen keskiarvo on: "  + str(keskiarvo))


#tehtävä 5
#kysytään käyttäjältä tavarat.
leiviska1 = float(input("Syötä leivisköjen määrä: "))
naula1 = float(input("Syötä naulojen määrä: "))
luoti1 = float(input("Syötä luotien määrä: "))
#tavaroiden muunnokset grammoiksi
gramma1 = float(20 * 32 * 13.3 * leiviska1)
gramma2 = float(32 * 13.3 * naula1)
gramma3 = float(13.3 * luoti1)

yhteispaino = gramma1 + gramma2 +gramma3
#printataan vastaus kilogrammoissa ja grammoissa
print(f"Massa nykymittojen mukaan: \n"
      f"{yhteispaino // 1000} kilogrammaa ja"
      f" {yhteispaino % 1000:.2f} grammaa")

#tehtävä 6

#haetaan random
import random
#tehdään randomisti generoitu lista kolmelle ja neljälle numerolle.
kolminumeroinen_koodi = [random.randint(0, 9) for cum in range(3)]
print(f"Kolminumeroinen koodinne: {kolminumeroinen_koodi}")

nelinumeroinen_koodi = [random.randint(1, 6) for o in range(4)]
print(f"Nelinumeroinen koodinne: {nelinumeroinen_koodi}")


# tein tämän näköisen aluksi, mutta en siitä, joten menin etsimään netistä ratkaisua
"""import random

numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)

input("Pyydä kolminumeroinen koodi painamalla enter.")
print(f"Kolminumeroinen koodi: {numero1, numero2, numero3}")

numero4 = random.randint(1, 6)
numero5 = random.randint(1, 6)
numero6 = random.randint(1, 6)
numero7 = random.randint(1, 6)

input("Pyydä nelinumeroinen koodi painamalla enter.")

print(f"Nelinumeroinen koodi: {numero4, numero5, numero6, numero7}")"""