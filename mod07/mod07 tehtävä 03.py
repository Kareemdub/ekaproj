"""Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja
tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta
kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)"""

la_ohjelma = True
la_sanakirja = {"EFHK": "Helsinki-Vantaan lentoasema", "EBBR": "Brussels Airport"}

print("Tervetuloa lentokenttien ICAO-koodijärjestelmään.")
kysely = input("Lisätäänkö lentokenttä, haetaanko lentokenttää vai lopetetaanko? [L/H/LOPETA]: ").upper().strip()


print(kysely)

while la_ohjelma:
    if kysely == "LOPETA":
        print("Poistutaan ohjelmasta.")
        la_ohjelma = False
    elif kysely == "L":
        print("Lopeta kirjoittamala LOPETA.")
        icao = input("Syötä ICAO-koodi: ").upper().strip()
        la_nimi = input("Syötä Lentokentän nimi: ")
        la_sanakirja[icao] = la_nimi
        print(f"ICAO-koodi on {icao} ja Lentokentän nimi: {la_nimi}. Lentokenttä lisätty listaan!")
        print(la_sanakirja)
        if icao or la_nimi == "LOPETA" or icao or la_nimi == "Lopeta":
            la_ohjelma = False
    elif kysely == "H":
        print("Haetaan lentokenttä")
        icao = input("Anna ICAO-koodi. Jos haluat lopettaa, kirjoita 'LOPETA': ").upper().strip()
        if icao == "LOPETA":
            print("Ohjelma lopetaan")
            la_ohjelma = False
        elif icao in la_sanakirja:
            print(f"ICAO-koodin {icao} lentokenttä on", la_sanakirja[icao])

        elif not icao in la_sanakirja:
            print("Lentokenttää ei löytynyt")

    else:
        print("Virheellinen syöttö. Lopetetaan ohjelma.")
        la_ohjelma = False
