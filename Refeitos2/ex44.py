entrada = [5, 3, 9, 1, 10]
def encontrar_maior(lista):
    maior_numero = lista[0]
    
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
        return maior_numero

saida = encontrar_maior(entrada)
print(saida)