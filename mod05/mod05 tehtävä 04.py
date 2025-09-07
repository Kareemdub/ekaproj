#tehtävä 4

kaupungit = []

for nimi in range(5): #asetetaan 5 listan rangeksi?
    kaupunki = input("Syötä yksitellen viisi kaupungin nimeä: ") # pyydetään 5 nimeä
    kaupungit.append(kaupunki) #lisätään listaan nimet

for nimi in kaupungit: #for lauseke on hieman outo minulle vielä, ja en kunnolla ymmärrä sen käyttöä
    print(nimi) # printataan nimet