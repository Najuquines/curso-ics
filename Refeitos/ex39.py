entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def numeros_pares(lista):
    
    numeros_pares_lista = []
    
    for numero in lista:
     
        if numero % 2 == 0:
            
         numeros_pares_lista.append(numero)

    return numeros_pares_lista

saida = numeros_pares(entrada)

print(saida)