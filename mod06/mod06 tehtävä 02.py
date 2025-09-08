#tehtävä 2

import random

tahko = input("Anna nopan tahkot: ")

def heitto(tahko):
    noppa = random.randint(1, int(tahko))
    return noppa


while True:
    nopat = heitto(tahko)
    print(f"Noppa osui numeroon {nopat}")
    if nopat == int(tahko):
        break
print("Noppa osui suurimpaan numeroon!")
