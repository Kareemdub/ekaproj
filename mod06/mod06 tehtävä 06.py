#tehtävä 6
import math
#kysytään pitsatiedot
halkaisija1 = float(input("Anna ensimmäisen pitsan halkaisija senttimetreinä: "))
halkaisija2 = float(input("Anna toisen pitsan halkaisija senttimetreinä: "))
euro1 = float(input("Anna ensimmäisen pitsan eurohinta: "))
euro2 = float(input("Anna toisen pitsan eurohinta: "))

#pitsalaskuri funktio
def pitsa_laskuri(halkaisija1, halkaisija2, euro1, euro2):
    eka_pitsa = halkaisija1 * math.pi
    toka_pitsa = halkaisija2 * math.pi
    hinta1 = eka_pitsa / 100 * euro1
    hinta2 = toka_pitsa / 100 * euro2
    return hinta1, hinta2

#asetetaan muuttujat ja printataan pitsojen hinnat
eka_pitsa, toka_pitsa = pitsa_laskuri(halkaisija1, halkaisija2, euro1, euro2)
print(type(pitsa_laskuri))
print(f"Ensimmäisen pitsan hinta on {eka_pitsa:.2f}€/m2 ja toisen pitsan hinta on {toka_pitsa:.2f}€/m2")

#selvitetään kumpi pitsa on halvempi
if eka_pitsa < toka_pitsa:
    print("Ensimmäisen pitsan hintasuhde on halvempi")
elif toka_pitsa < eka_pitsa:
    print("Toisen pitsan hintasuhde on halvempi")
else:
    print("Pitsoilla on sama hintasuhde!")