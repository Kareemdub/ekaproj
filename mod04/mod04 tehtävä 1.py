#mod 04 tehtävät
import random

#tehtävä 1

kolmet = 0

while kolmet < 999:
    kolmet = kolmet + 3
    print(kolmet)

#tehtävä 2

tuuma_ohjelma = True
while tuuma_ohjelma:
    tuuma = float(input("Anna tuumat: "))
    tuuma_tulos = tuuma * 2.54
    if tuuma_tulos < 0:
        tuuma_ohjelma = False
    else:
        print(tuuma_tulos)

#tehtävä 3
isoin_numero = 0
pienin_numero = 0


while True:
    numero = input("Anna numero tai paina enter lopettaaksesi: ") #pyydetään numero käyttäjältä
    if numero == "": #jos merkkijono on tyhjä, lopetetaan ohjelma.
        break
    fnumero = int(numero) #muutetaan syöttö integeriksi
    if isoin_numero is 0 or pienin_numero is 0: # jos ei syötetä numeroa
        pienin_numero = fnumero
        isoin_numero = fnumero
    elif fnumero < pienin_numero: # Jos pienin numero on suurempi kuin syötetty, laitetaan se uudeksi pienimmäksi
        pienin_numero = fnumero
    elif fnumero > isoin_numero:  # Jos isoin numero on pienempi kuin syötetty numero, laitetaan se uudeksi isoimmaksi
        isoin_numero = fnumero

print(f"Pienin numero on {pienin_numero}")
print(f"Isoin numero on {isoin_numero}")







"""merkkijono_ohjelma = True
while merkkijono_ohjelma:
    luku = input("anna luku: ")
    if luku == "":
        merkkijono_ohjelma = False"""



"""


#tehtävä 6 (horror)

N = input("Anna ")
# TODO Kysy N arvo käyttäjältä
n = 0
i = 0

while i < N:
    i += 1
    #arvotaan satunnainen piste koordinaatistoon
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste on {x}, {y}")
    # TODO testaa toteutuuko piste epäyhtälön x^2+y^2 < 1
    #jos ehto on totta, kasvata n-laskurin arvo
# TODO laske piin likiarvo käyttäen kaavaa π≈4n/N

"""