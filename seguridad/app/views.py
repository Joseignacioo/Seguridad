from django.http import HttpResponse
from .forms import *
from django.shortcuts import render , redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Usuario
from .forms import CustomAuthenticationForm
# Create your views here.

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                # Redirige a la página deseada después de iniciar sesión
                return redirect('crear_usuario')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})



def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo despues que se ejecute
    else: 
        form = UsuarioForm()
    return render(request, 'dashboard/crear_usuario.html', {'form': form})

@login_required
def listar_usuario(request):
    datos = Usuario.objects.all()    
    data = {
        'consultas': datos
    }
    return render(request, 'dashboard/listar_usuario.html',data)

@login_required
def salir(request):
    logout(request)
    return redirect('home')
