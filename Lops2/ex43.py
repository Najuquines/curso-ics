# Lista de entrada
entrada = [-10, 15, -20, 25, 30]

# Função para retornar uma nova lista onde todos os números negativos foram removidos
def remover_negativos(lista):
    # Inicializa uma lista vazia para armazenar os números positivos
    nova_lista = []
    
    # Itera sobre cada número na lista de entrada
    for numero in lista:
        # Verifica se o número é positivo ou zero
        if numero >= 0:
            # Se o número for positivo ou zero, adiciona à nova lista
            nova_lista.append(numero)
    
    # Retorna a nova lista sem os números negativos
    return nova_lista

# Chama a função passando a lista de entrada como argumento e armazena o resultado em uma variável
saida = remover_negativos(entrada)

# Imprime a nova lista resultante
print(saida)