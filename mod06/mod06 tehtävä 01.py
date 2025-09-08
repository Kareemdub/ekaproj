#tehtää 1
import random

def heitto():
    noppa = random.randint(1, 6)
    return noppa

while True:
    noppa = heitto()
    print(f"Noppa osui numeroon {noppa}")
    if noppa == 6:
        break

print("Noppa osui kutoseen!")