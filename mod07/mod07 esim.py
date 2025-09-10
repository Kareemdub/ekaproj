#monikko eli (tuple) on kuin lista jota ei voi muokata

lista = [1 ,2 ,3 ,4 ,5]

monikko = (13 ,24,3 ,4 ,25)
monikko2 = 1 ,2 ,3 ,4 ,5


print(monikko)


monikko3 = (1 ,2 ,"Ulla")

luku = monikko[3]
print("Hain monikosta luvun", luku)

print(lista[0])
print(monikko[0])

lista[0] = 0
print("muokattu lista", lista)

lista.append(7)
print(lista)

i = 0
for luku1 in monikko:
    print(f"Monikon {i + 1}. luku on {luku1}")
    i = i + 1


sanat = "yksi", "kaksi", "kolme", "neljä", "viisi"
for sana in sanat:
    print(sana)
    if sana == "kolme":
        print("Sana kolme löytyi")

for i, sana in enumerate(sanat):
    print(f"Monikon {i + 1}. luku on {sana}")

if "kolme" in sanat:
    print("sana viides löytyi")


hedelmat = ("Sitruuna", "Omena", "Banaani")
(eka, toka, kolmas) = hedelmat
print("Monikko purettu muuttujiin,", eka, toka, kolmas)

#monikon voi antaa funktiolle parametrinä
print("funktio käyttö")
def tulosta_monikko(hedelmat):
    for h in hedelmat:
        print(h)

tulosta_monikko(hedelmat)


#monikko funktion paluuarvona
import random

def heita():
    #luodaan tuple, eli monikko ja puretaan muuttujiin
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    return eka ,toka

noppa1, noppa2 = heita()
print("funkiosta palautuu arvot", noppa1 ,noppa2)
print("---------------------------------")

#joukko eli set{}

joukko = {1, 2, 3, 4, 5, 6}
print(joukko)
llista = [1,2,3,4,5,6,6]
mmonikko = 1,23,4,5,6,6,6
jjoukko = {6,1,2,3,4,5,6,6,6}
print(jjoukko)

jjoukko.add(6)
jjoukko.add(7)
print(jjoukko)

autojoukko = set()
autojoukko.add("Audi")
print(autojoukko)
print(type(autojoukko))

autosanakirja = {}
print("SANAKIRJA")





oppilaat = {"Aapeli": 25,
            "Petteri" : 21,
            "Joonas" : 23,
            "Emma" : 30
}

print(oppilaat)
print(oppilaat.items())
print(oppilaat.keys())
print(oppilaat.values())


for o in oppilaat: #kierrosmuuttuja o saa arvokseen sanakirjan avaimet
    print(o)

avain = "Aapeli"
oppilaat[avain]
print("Etsitään avaimella Aapeli, hänen ikä", oppilaat[avain])

print("Joonaksen ikä", oppilaat["Joonas"])

for o in oppilaat:
    print(f"Oppilaan nimi on {o} ja ikä on {oppilaat[o]}")

#hae emman ikä if in
nimi = input("Syötä oppilaan nimi: ")
if nimi in oppilaat:
    ika = oppilaat[nimi] #haetaan avaimella arvo
    print(f"oppilas on {nimi} ja ikä on {ika}")
else:
    print(f"Nimeä {nimi} ei löytynyt")





numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

print (numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print (f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")



yhteystiedot = {"Aapeli": {"puh" : "0123", "osoite": "lintutie 5"},
               "Petteri" : {"puh" : "4567", "osoite": "jee123"},
               "Joonas" : {"puh" : "3333"},
                "Emma" : {"puh" : "0495"}
}

print(f"Aapelin puhelinnumero:  {yhteystiedot["Aapeli"]["puh"]}")

oppilaat2 = {"Aapeli": 25,
            "Petteri" : 21,
            "Joonas" : 23,
            "Emma" : 30
            }
#lisätään uusi oppilas
#lisätään avaimen avulla, mikäli avain jo löytyy tämä päivittää tiedot

oppilaat2["Ulla"] = 22
oppilaat2["Aapeli"] = 69

print (oppilaat2)

