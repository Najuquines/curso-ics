from django.shortcuts import render

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

def Cadastr(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        cidade = request.POST.get('cidade')
        telefone= request.POST.get('telefone')
        estado = request.POST.get('estado')
        email = request.POST.get('e-mail')
        CPF = request.POST.get('CPF')
        cadastro = Cadastr(nome=nome, email=email, idade=idade, cidade=cidade, telefone=telefone, estado=estado, CPF=CPF)
        cadastro.save()
        dados = {
            'mensagem': 'Seu cadastro foi execultado com sucesso!'
        }

        return render(request, 'cadastro.html', dados)
    else:
        return render(request, 'cadastro.html')