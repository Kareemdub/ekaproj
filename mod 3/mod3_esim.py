#valintarakenne esim.
from random import randint
#onko_totta = False
onko_totta = 3 < 1

satunnaisluku = randint(0, 100)
print(f"Arvottu luku: {satunnaisluku}")

#kolikonheittosimulaattori

if satunnaisluku < 50:
    print("Kruuna")
elif satunnaisluku > 50:
    print ("Klaava")
else: # totetutuu kun arvottu luku on tasan 50 (1/101)
    print ("Kolikko pystyssä")


if onko_totta:
    print("tosi on!")
else:
    print("epätosi!")

print("if lauseen jälkeinen teksti")

#dummy kirjautuminen
oikea_salasana = "salakala"
oikea_tunnus = "kala"

input_salasana = input("Anna salasana:")
input_tunnus = input("Anna tunnus")
if input_salasana == oikea_salasana and input_tunnus == oikea_tunnus:
    print("Kirjautuminen onnistui")
    kehote = input("Mitä haluat tehdä? ")
    if kehote == "tervehtiä":
        print("no morjens")
    else:
        print("en ymmärrä kehotetta")
else:
    print("väärin ")



print("Ohjelma suljettu.")

