# Lista de entrada
entrada = [1, 2, 3, 4, 5]

# Função para retornar uma lista com os elementos na ordem inversa
def inverter_ordem(lista):
    # Inicializa uma lista vazia para armazenar os elementos na ordem inversa
    lista_invertida = []
    
    # Itera sobre a lista de entrada em ordem inversa
    for elemento in reversed(lista):
        # Adiciona cada elemento à lista invertida
        lista_invertida.append(elemento)
    # reversed a ordem dos elementos da lista é invertida.
    # Retorna a lista com os elementos na ordem inversa
    return lista_invertida

# Chama a função passando a lista de entrada como argumento e armazena o resultado em uma variável
saida = inverter_ordem(entrada)

# Imprime a lista resultante
print(saida)