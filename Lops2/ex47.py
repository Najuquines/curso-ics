# Lista de entrada
entrada = ["maçã", "banana", "cereja"]

# Elemento a ser verificado
e = "banana"

# Função para verificar se o elemento está na lista
def verificar_elemento_na_lista(lista, elemento):
    # Itera sobre cada elemento na lista de entrada
    for item in lista:
        # Verifica se o elemento atual é igual ao elemento que estamos procurando
        if item == elemento:
            # Se encontrado, retorna True
            return True
    
    # Se o elemento não for encontrado após percorrer toda a lista, retorna False
    return False

# Chama a função passando a lista de entrada e o elemento a ser verificado como argumentos
resultado = verificar_elemento_na_lista(entrada, e)

# Imprime o resultado
print(resultado)