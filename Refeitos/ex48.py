def inverter_ordem(lista):
  
    lista_invertida = []
    
    for elemento in reversed(lista):

        lista_invertida.append(elemento)
  
    return lista_invertida
saida = inverter_ordem(entrada)
print(saida)