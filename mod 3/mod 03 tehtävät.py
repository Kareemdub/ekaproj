#mod 3 tehtävät
#tehtävä 1
#from statistics import median

kuha = float(input("Anna kuhan pituus senttimetreinä: "))

if kuha >= 37:
    print("Kuha on mainio!")
else:
    print(f"Kuha on {37 - kuha} senttiä minimi pyyntipituudesta"
          f"'laske kuha takaisin veteen")


#tehtävä 2

input_luokka = input("Anna hyttiluokka: ")


if input_luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella")
elif input_luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif input_luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif input_luokka == "C":
    print("C on ikkunaton hytti autokanen alapuolella")
else:
    print("Virheellinen hyttiluokka.")

#tehtävä 3


sukupuoli = input("Anna biologinen sukupuoli: ")

if sukupuoli == "mies":
    mies_hemoglobiini = float(input("Kerro hemogloiiniarvo muodossa g/l: "))
    if 133 < mies_hemoglobiini < 196:
        print("Hemoglobiini on normaali")
    elif mies_hemoglobiini > 196:
        print("Hemoglobiini on korkea:(")
    else:
        print("Hemoglobiini on alhainen:(")
elif sukupuoli == "nainen":
    nainen_hemogloiini = float(input("Kerro hemogloiiniarvo muodossa g/l: "))
    if 116 < nainen_hemogloiini < 176:
        print("Hemoglobiini on normaali")
    elif nainen_hemogloiini > 175:
        print("Hemoglobiini on korkea:(")
    else:
        print("Hemoglobiini on alhainen:(")
else:
    print("sukupuolta ei löydy")

#tehtävä 4
#pitää miettiä lisää
vuosiluku = float(input("Anna vuosiluku: "))
if int(vuosiluku / 4) :
    print("vuosiluku on karkausvuosi")
else:
    print("vuosiluku ei ole karkausvuosi")
