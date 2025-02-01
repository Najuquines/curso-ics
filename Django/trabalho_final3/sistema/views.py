from django.shortcuts import render
from cadastro.models import Cadastro
from aulas.models import Curso

def home(request):
    return render(request, 'home.html')

def aulas(request):
    return render(request, 'aulas.html')

def cursos(request):
    return render(request, 'cursos.html')

def adm(request):
    return render(request, 'adm.html')

def infor(request):
    return render(request, 'infor.html')

def ven(request):
    return render(request, 'ven.html')

def enviar(request):
    return render(request, 'enviar.html')

def tela_cadastro(request):
    if request.method == 'POST':
        _primeiro_e_ultimo_nome = request.POST.get('primeiro_e_ultimo_nome')
        _idade = request.POST.get('idade')
        _cidade_e_estado = request.POST.get('cidade_e_estado')
        _telefone= request.POST.get('telefone')
        _email = request.POST.get('e-mail')
        _cpf = request.POST.get('cpf')
        cadastro = Cadastro(
            primeiro_e_ultimo_nome=_primeiro_e_ultimo_nome, 
            email=_email, 
            idade=_idade, 
            cidade_e_estado=_cidade_e_estado, 
            telefone=_telefone, 
            cpf=_cpf)
        cadastro.save()

        cursos = Curso.objects.all()
        dados = {
            'mensagem': 'Seu cadastro foi execultado com sucesso!',
            'cursos': cursos
        }

        return render(request, 'cadastro_confirmacao.html', dados)
    else:
        return render(request, 'cadastro.html')