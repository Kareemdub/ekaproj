#kommentti
"""paljon
kommentti"""

import math
import random

nimi= input("anna nimesi: ") #palauttaa merkkijonon str
ika = 20 # kokonaisluku int
ika_ensi_vuonna = ika + 1
str_ika_ensi_vuonna = str (ika_ensi_vuonna) # -> "21"
tervehdys = "Moi " + nimi + " " + str(ika_ensi_vuonna)


print(tervehdys)

#laskukone

#luetaan käyttäjältä kaksi lukua (str) jotka muunnetaan samantien
#liukuluvuiksi ja sijoitetaan muuttujiin
luku1 = float(input("anna ensimmäinen luku: "))
luku2 = float(input("anna toinen luku: "))

tulos= float(luku1) + float(luku2) #
#tulos= int(luku1) + int(luku2) #kokonaislukujen yhteenlasku
#tulos =1+2 # 3
tulos_yhteenlasku = luku1+ luku2
tulos_vahennuslasku = luku1 - luku2
tulos_jakolasku = luku1 / luku2
tulos_kertolasku = luku1 * luku2
kokonaisosa = luku1 // luku2
jakojaannos = luku1 % luku2


print("yhteenlaskuntoimituksen tulos: " +str(tulos_yhteenlasku)) # merkkijonot yhdistetään tarvitsee lukumuuttujan
print("vähennyslaskun tulos: " +str(tulos_vahennuslasku))
print("jakolaskun tulos: " +str(tulos_jakolasku))
print(f"kertolasku tulos: {tulos_kertolasku:}") # tulosteen muotoilu f-stringillä (kannattaa)
print(f"jakolaskus tulos: {tulos_jakolasku:.2f}, jossa kokonaisosa on "
      f"{kokonaisosa} desimaaliosa {tulos_jakolasku - kokonaisosa}"
      f" jakojäännös on {jakojaannos}")


#ympyrän pinta-ala pi * r^2: 3.149 x r^2
#piin arvo
print(math.pi)

#satunnaisluvun generointi 1-6
print(random.randint(1, 6))