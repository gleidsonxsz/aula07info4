from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')