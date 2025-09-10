#tehtävä 1

#monikko tammi-joulu

kuukaudet = (
    "talvi",
    "talvi",
    "kevät",
    "kevät",
    "kevät",
    "kesä",
    "kesä",
    "kesä",
    "syksy",
    "syksy",
    "syksy",
    "talvi",
)

kuukauden_numero = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukauden_numero <= 12:
    print(kuukaudet[kuukauden_numero-1])
else:
    print("Väärä numero")