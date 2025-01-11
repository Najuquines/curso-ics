entrada = ["maçã", "banana", "kiwi", "abacate", "uva"]
def palavras_mais_de_4_caracteres(lista):
    palavras_lista = []
    
    for palavra in lista:
        
        if len(palavra) > 4:

            palavras_lista.append(palavra)

    return palavras_lista
saida = palavras_mais_de_4_caracteres(entrada)
print(saida)