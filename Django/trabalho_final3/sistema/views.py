from http.client import HTTPResponse
from django.shortcuts import render
from cadastro.models import Cadastro
from aulas.models import Curso
from aulas.models import Aulas

def home(request):
    return render(request, 'home.html')

def aulas(request):
    return render(request, 'aulas.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

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
        _email = request.POST.get('email')
        _cpf = request.POST.get('cpf')
        cadastro = Cadastro(
            primeiro_e_ultimo_nome=_primeiro_e_ultimo_nome, 
            email=_email, 
            idade=_idade, 
            cidade_e_estado=_cidade_e_estado, 
            telefone=_telefone, 
            cpf=_cpf)
        cadastro.save()

        dados = {
            'mensagem': 'Seu cadastro foi execultado com sucesso!'
        }

        return render(request, 'cadastro_confirmacao.html', dados)
    else:
        return render(request, 'cadastro.html')
    

def detalhes_cursos(request):
  cursos = Curso.objects.all()
  return render(request, 'detalhes-curso.html', {'cursos': cursos})

def curso_detalhe(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'curso-detalhe.html', {'curso': curso})

def administracao(request):
    if request.method == 'POST':
     _titulo = request.POST.get('titulo')
     _descricao = request.POST.get('descricao')
     _link = request.POST.get('link')
     
     administracao = Aulas(
         nome =_titulo,
         descricao = _descricao,
         link = _link
       
     )
     administracao.save()
     administracao = Aulas.objects.all()
    return render(request, 'administracao.html',{'administracao': administracao} )
  