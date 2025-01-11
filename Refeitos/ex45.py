def verificar_elemento_na_lista(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
        
        return False

resultado = verificar_elemento_na_lista(entrada, e)
print(resultado)