import sys

def elementos_comuns(lista1, lista2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))

lista1 = list(sys.stdin.readline().split())
lista2 = list(sys.stdin.readline().split())

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")



# def elementos_comuns(lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     return list(set1.intersection(set2))

# lista1 = list(input().split())
# lista2 = list(input().split())

# if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
#     comuns = elementos_comuns(lista1, lista2)
#     print(f"Elementos comuns às duas listas: {comuns}")
# else:
#     print("Entrada inválida.")
