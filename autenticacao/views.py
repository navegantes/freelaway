from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


# Create your views here.
def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/plataforma')

    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')

        # user = User.objects.filter(username=username)

        # if user.exists():
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR,
                                 'Já existe um usário com esse username')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username,
                                            password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')

            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/jobs/encontrar_jobs')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/jobs/encontrar_jobs')


def sair(request):
    auth.logout(request)
    return redirect('/auth/login')
