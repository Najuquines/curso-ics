entrada = ["sol", "lua", "sol", "estrela", "lua", "lua"]
def contar_ocorrencias(lista):
    contagem = {}
    
    for elemento in lista:
        if elemento in contagem:
    
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    
    return contagem
saida = contar_ocorrencias(entrada)
print(saida)