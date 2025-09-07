#tehtävä 2

lista = []

numero = input("Anna luku: \n"
        "paina enter lopettaaksesi") #pyydettän luku käyttäjältä

while numero != "": #luupataan kunnes painetaan enter
    inumero = int(numero) #muutetaan syöttö int arvoksi, että lista osaa tulkita sen oikein
    lista.append(inumero) #listätään numero listaan
    numero = input("Anna luku: ")

lista.sort(reverse=True) #laitetaan lista järjestykseen ja käännetään se väärinpäin
print(lista[0:5]) #printataan 5 ensimmäistä lukua listasta