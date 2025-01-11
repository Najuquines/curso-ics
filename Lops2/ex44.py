# Lista de entrada
entrada = ["sol", "lua", "sol", "estrela", "lua", "lua"]

# Função para contar e retornar um dicionário com a contagem de cada elemento
def contar_ocorrencias(lista):
    # Inicializa um dicionário vazio para armazenar a contagem de cada elemento
    contagem = {}
    
    # Itera sobre cada elemento na lista de entrada
    for elemento in lista:
        # Verifica se o elemento já está no dicionário
        if elemento in contagem:
            # Se o elemento já existe no dicionário, incrementa o contador em 1
            contagem[elemento] += 1
        else:
            # Se o elemento não existe no dicionário, adiciona-o com o contador iniciado em 1
            contagem[elemento] = 1
    
    # Retorna o dicionário com a contagem de cada elemento
    return contagem

# Chama a função passando a lista de entrada como argumento e armazena o resultado em uma variável
saida = contar_ocorrencias(entrada)

# Imprime o dicionário resultante
print(saida)