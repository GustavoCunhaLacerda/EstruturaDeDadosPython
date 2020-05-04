lista = [94, 7, 3, 12, 56]
lista[3]
len(lista)-1

# Busca linear em lista sequencial O(n)
def busca(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None    

lista_estranha = [8, "5", 32, 0, "python", 11]
elemento = "python"

indice = busca(lista_estranha, elemento)
if indice is not None:
    print(f"O índice do elemento {elemento} é {indice}.")
else:
    print(f"O elemento {elemento} não se encontra na lista.")

# Inserção e remoção de elemento O(n)
""" 
    Para inserir ou remover um elemento é necessário, se não for no final da lista,
    mover elementos.
"""
