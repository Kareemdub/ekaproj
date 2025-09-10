"""tehtävä 2
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää
 tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin
  Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
  Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
   Käytä joukkotietorakennetta nimien tallentamiseen.
"""

nimet = set()
sanasetti = True

while sanasetti:
    nimi = input("Anna nimi: ").capitalize().strip()
    if nimi == "":
        sanasetti = False
    elif nimi in nimet:
        print("Nimi löytyy jo")
    else:
        nimet.add(nimi)
        print("Uusi nimi")


for nimi in nimet:
    print(nimi)
