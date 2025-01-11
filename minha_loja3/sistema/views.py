from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')
def contato(request):
    return render(request, 'contato.html')

def produtos(request):

    Dados = {
    'produtos': [
        {
            'nome': 'Esmalte Vermelho Intenso',
            'marca': 'Risqué',
            'tipo': 'Esmalte',
            'cor': 'Vermelho',
            'preco': 12.99
        },
        {
            'nome': 'Removedor de Esmalte Sem Acetona',
            'marca': 'Impala',
            'tipo': 'Removedor',
            'preco': 8.50
        },
        {
            'nome': 'Base Fortalecedora',
            'marca': 'Colorama',
            'tipo': 'Base',
            'preco': 10.99
        },
    ]
    }
        
    return render(request, 'produtos.html', Dados)



