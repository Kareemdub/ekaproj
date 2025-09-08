#tehtävä 5

lista = [1, 2, 3, 4, 5, 6, 7, 8]

def lista_ohjelma(lista):
    lista2 = lista.copy()
    del lista2[0:7:2]
    return lista2

lista_ohjelma(lista)
print(f"Alkuperäinen lista {lista}")
print(f"Päivitetty lista {lista_ohjelma(lista)}")

