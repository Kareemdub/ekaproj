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
#testataan laskutapaa (clueless)
gramma1 = float(20 * 32 * 13,3 * leiviska1)
gramma2 = float(32 * 13,3 * naula1)
gramma3 = float(13.3)

print(f"grammat: {gramma1 + gramma2 + gramma3}")
