
entrada = [10, 20, 30, 40, 50]

def calcular_media(lista):
    soma = 0

    for valor in lista:
        soma += valor
    media = soma / len(lista)
    return media
saida = calcular_media(entrada)
print(saida)