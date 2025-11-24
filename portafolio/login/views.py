from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from .forms import RegistroForm, LoginForm
from .mixins import LoginRequiredCustomMixin, solo_login_requerido

# Nota: Los mixins se usan en vistas basadas en clases (CBV)
# Ejemplo: class LogoutView(LoginRequiredCustomMixin, View):
# En este proyecto usamos FBV (Function-Based Views) por simplicidad


def registro(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            # Mostrar errores del formulario
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}", extra_tags='danger')
    else:
        form = RegistroForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Verificar si el usuario existe
            if not User.objects.filter(username=username).exists():
                messages.error(request, f'El usuario "{username}" no existe.', extra_tags='danger')
                return render(request, 'login.html', {'form': form})
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'La contraseña es incorrecta.', extra_tags='danger')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


@solo_login_requerido
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


# ============= EJEMPLO DE VISTAS BASADAS EN CLASES CON MIXINS =============
# Los mixins LoginRequiredCustomMixin se pueden usar con CBV de la siguiente forma:
#
# class LogoutView(LoginRequiredCustomMixin, View):
#     """Vista de logout usando mixin - redirige a login si no está autenticado"""
#     def get(self, request):
#         logout(request)
#         return render(request, 'logout.html')
#
# En urls.py se registraría como:
# path('logout/', LogoutView.as_view(), name='logout')
#
# El proyecto actualmente usa Function-Based Views (FBV) con decoradores
# pero los mixins están disponibles para usar con CBV si se necesita refactorizar
