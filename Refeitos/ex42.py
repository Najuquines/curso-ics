entrada = [-10, 15, -20, 25, 30]
def remover_negativos(lista):
   
    nova_lista = []
    for numero in lista:
 
        if numero >= 0:
   
            nova_lista.append(numero)

    return nova_lista
saida = remover_negativos(entrada)
print(saida)