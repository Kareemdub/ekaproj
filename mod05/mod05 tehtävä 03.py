#tehtävä 3

alkuluku = True
luku = int(input("Anna luku: "))

if luku == 0 or luku == 1: # 0 tai 1 ei ole alkulukuja
    alkuluku = False
elif luku > 1:
    for jakaja in range(2, luku): #laitetaan jakajan rangeksi 2 - syötetty luku
        if (luku % jakaja) == 0: #jaetaan syötetty luku jokaisella luvulla kahden ja syötetyn luvun välillä
            print(f"Luku on jaollinen luvulla {jakaja}") #jos luku on jaollinen jollain luvulla, printataan se
            alkuluku = False
    #else:
  #      print("luku on alkuluku") #jos luku on jaollinen, kerrotaan että se ei ole alkuluku

if alkuluku:
    print("Numero on alkuluku")
else:
    print("Numero ei ole alkuluku")