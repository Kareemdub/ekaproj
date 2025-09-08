#tehtävä 3

litra = 3.785

def gallona(litra):
    syotetty_gallona = float(input("Anna Gallonamäärä: "))
    muunnos = syotetty_gallona * litra

    return muunnos

while True:
    litrat = gallona(litra)
    if litrat > -1:
        print(f"Galloonat ovat {litrat} litroina. Kirjoita miinusluku lopettaaksesi")
    else:
        break
print("Ohjelma sulkeutuu")

