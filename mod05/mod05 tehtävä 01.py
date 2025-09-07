#mod 05 tehtävät


#tehtävä 1
import random

summa = 0 #summa muuttuja
arpa = [] #tehdään arpa lista
arpojen_maara = input("Lisää arpa painamalla enter tai lopeta kirjoittamalla jotain:") #lisätään noppa joka enteristä

while arpojen_maara == "": #kun painetaan vain enteriä, heitetään noppaa 1-6
    arpa1 = random.randint(1, 6)
    arpa.append(arpa1) #lisätään nopan luku listaan
    arpojen_maara = input("Lisää arpa painamalla enter tai lopeta kirjoittamalla jotain:")

for i, kuutio in enumerate(arpa): # for loop arpa listalle, pitäen kirjaa arpojen määrästä enumerate funktiolla
    summa = summa + kuutio
    print(f"arpa {i + 1} on {kuutio}")

print(f"noppien lukujen summa on {summa}") # tulostetaan silmälukujen summa

