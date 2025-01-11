entrada = [1, 2, 3, 4, 5]
def quadrado_numeros_impares(lista):
    quadrados_impares = []
    
    for numero in lista:
        if numero % 2 != 0:
            quadrados_impares.append(numero ** 2)
    
    return quadrados_impares

saida = quadrado_numeros_impares(entrada)
print(saida)
