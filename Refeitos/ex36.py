def verificar_palindromo(texto):
    texto = texto.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
  
    return texto == texto[::-1]

texto_usuario = input("Insira uma palavra ou frase: ")

if verificar_palindromo(texto_usuario):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")