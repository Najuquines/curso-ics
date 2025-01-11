num1 = input('Digite um numero: ')
num2 = input('Digite o segundo numero: ')
operação = input('Digite qual operacao voceê deseja: ((+ - * / ')

if operação == '+':
    soma = int(num1) + int(num2)
    print(soma)
elif operação == '-':
    subtração = int(num1) - int(num2)
    print(subtração)
elif operação == '*':
    multiplicação = int(num1) * int(num2)
    print(multiplicação)
elif operação == '/':
    divisão = int(num1) / int(num2)
    print(divisão)

