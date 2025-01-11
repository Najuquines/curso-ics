# Lista de entrada
entrada = [10, 20, 30, 40, 50]

# Função para calcular e retornar a média dos valores da lista
def calcular_media(lista):
    # Inicializa a variável soma com zero
    soma = 0
    
    # Itera sobre cada valor na lista de entrada
    for valor in lista:
        # Adiciona o valor atual à soma
        soma += valor
    
    # Calcula a média dividindo a soma pelo número total de valores na lista
    media = soma / len(lista)
    
    # Retorna a média calculada
    return media

# Chama a função passando a lista de entrada como argumento e armazena o resultado em uma variável
saida = calcular_media(entrada)

# Imprime a média calculada
print(saida)