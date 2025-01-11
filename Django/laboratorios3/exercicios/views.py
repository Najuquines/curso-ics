from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ex1(request):
    return render(request, 'ex1.html')

def ex2(request):
    data = {
        'titulo': 'Exercicio 2 ',
        'descricao':  'some um valor com o outro e imprima o resultado'

    }
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        total = int(valor1) + int(valor2)
        data['total'] = total
    return render(request, 'ex2.html', data)

def ex3(request):
    data = {'titulo': 'Exercicio 3 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        frase = f"seu nome {nome} e sua idade é {idade}"
        data ['frase'] = frase
    return render(request, 'ex3.html', data)

def ex4(request):
    data = {'titulo': 'Exercicio 4',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        soma = int(valor1) + int(valor2)
        data['soma'] = soma
    return render (request, 'ex4.html', data)

def ex5(request):
    data = {'titulo': 'Exercicio 5',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        palavra = request.POST.get("palavra") 
        if palavra:
            caracteres = len(palavra)
            data['caracteres'] = caracteres
        else:
            data['caracteres'] = 0  
    return render(request, 'ex5.html', data)

def ex6(request):
    data = {'titulo': 'Exercicio 6 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        palavra3 = request.POST.get("palavra3")
        palavra4 = request.POST.get("palavra4")
        palavra5 = request.POST.get("palavra5")
        frase = str(palavra1) + " " + str(palavra2) + " " + str(palavra3) + " " + str(palavra4) + " " + str(palavra5)
        data['frase'] = frase
    return render (request, 'ex6.html', data)

def ex7(request):
    data = {'titulo': 'Exercicio 7 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + int(valor)
        data['soma'] = soma
    return render (request, 'ex7.html', data)

def ex8(request):
    data = {'titulo': 'Exercicio 8',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + 1
        data['soma'] = soma
    return render (request, 'ex8.html', data)

def ex10(request):
    data = {'titulo': 'Exercicio 10',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + int(valor)
        data['soma'] = soma
    return render (request, 'ex10.html', data)

def ex11(request):
    data = {'titulo': 'Exercicio 11 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        palavra = request.POST.get("palavra") 
        if palavra:
            caracteres = len(palavra)
            data['caracteres'] = caracteres
        else:
            data['caracteres'] = 0  
    return render(request, 'ex11.html', data)

def ex9(request):
    data = {'titulo': 'Exercicio 9 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        nome = request.POST.get('nome')
        frase = f'Olá, {nome}'
        data['frase'] = frase
    return render (request, 'ex9.html', data)

def ex12(request):
    data = {'titulo': 'Exercicio 12 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra1) + " " + str(palavra2) + " " 
        data['frase'] = frase
    return render (request, 'ex12.html', data)

def ex13(request):
    data = {'titulo': 'Exercicio 13 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        Ano_de_nascimento = request.POST.get("ano_de_nascimento") 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(Ano_de_nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex13.html', data)

def ex15(request):
    data = {'titulo': 'Exercicio 15 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        frase = request.POST.get("frase") 
        frase1 = str(frase) + ' ' + str(frase) + ' ' + str(frase)
        data['frase1'] = frase1
    return render(request, 'ex15.html', data)

def ex14(request):
    data = {'titulo': 'Exercicio 14 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex14.html', data)

def ex17(request):
    data = {'titulo': 'Exercicio 17 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " " + str(palavra1) + " " 
        data['frase'] = frase
    return render (request, 'ex17.html', data)

def ex16(request):
    data = {'titulo': 'Exercicio 16 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        valor3 = request.POST.get("valor3") 
        valor4 = request.POST.get("valor4")
        media = (int(valor1) + int(valor2) + int(valor3) + int(valor4))/4
        data['media'] = media
    return render (request, 'ex16.html', data)
    
def ex20(request):
    data = {'titulo': 'Exercicio 20 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        total = int(valor1) + int(valor2)
        data['total'] = total
    return render(request, 'ex20.html', data)

def ex18(request):
    data = {'titulo': 'Exercicio 18 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " está a leste de " + str(palavra1)
        data['frase'] = frase
    return render(request, 'ex18.html', data)

def ex19(request):
    data = {'titulo': 'Exercicio 19 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        nome = request.POST.get('nome')
        frase = f'Olá {nome}'
        data['frase'] = frase
    return render (request, 'ex19.html', data)

def ex21(request):
    data = {'titulo': 'Exercicio 21',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}

    if request.method =='POST':
        frase = request.POST.get('frase')
        conta_caracteres = f'{len(frase)}'

        data['conta_caracteres'] = conta_caracteres
    return render (request, 'ex21.html', data)


def ex22(request):
    data = {'titulo': 'Exercicio 22 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        parte1 = request.POST.get("parte1") 
        parte2 = request.POST.get("parte2")
        nova_string = str(parte1) + " " + str(parte2)
        data['nova_string'] = nova_string
    return render (request, 'ex22.html', data)

def ex23(request):
    data = {'titulo': 'Exercicio 23 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        Ano_de_nascimento = request.POST.get("ano_de_nascimento") 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(Ano_de_nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex23.html', data)

def ex24(request):
    data = {'titulo': 'Exercicio 24 ',
        'descricao':  'saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex24.html', data)

def ex25(request):
    data = {'titulo': 'Exercicio 25 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex25.html', data)

def ex26(request):
    data = {'titulo': 'Exercicio 26 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        valor3 = request.POST.get("valor3") 
        valor4 = request.POST.get("valor4")
        media = (int(valor1) + int(valor2) + int(valor3) + int(valor4))/4
        data['media'] = media
    return render (request, 'ex26.html', data)

def ex27(request):
    data = {'titulo': 'Exercicio 27 ',
        'descricao':  'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " " + str(palavra1) + " " 
        data['frase'] = frase
    return render (request, 'ex27.html', data)

def ex28(request):
    data = {'titulo': 'Exercicio 28 ',
        'descricao':  'saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
}
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " está a leste de " + str(palavra1)
        data['frase'] = frase
    return render(request, 'ex28.html', data)
    

