from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm, LoginForm, RecetaDulceForm, RecetaBebidaForm, RecetaSaladaForm, RecetaDulce, RecetaBebida, RecetaSalada
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q


# Vista de registro
def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autenticar y loguear al usuario después de registrarse (opcional)
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido, ¡has iniciado sesión!')
            return redirect('home')  # Redirigir al home o donde desees
        else:
            messages.error(request, 'Hubo un error en el registro, revisa los datos.')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'register.html', {'form': form})

# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu_principal')  # Redirige al menú principal tras iniciar sesión
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')  # Redirigir al login después de cerrar sesión

# Vista para la página principal (home)
def home(request):
    return render(request, 'home.html')  # Asegúrate de que tienes un template llamado home.html



# Vista del menú principal con búsqueda
def menu_principal(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda desde el formulario
    resultados = []

    if query:
        # Buscar en el campo 'nombre_receta' de cada modelo
        resultados_dulces = RecetaDulce.objects.filter(Q(nombre_receta__icontains=query))
        resultados_saladas = RecetaSalada.objects.filter(Q(nombre_receta__icontains=query))
        resultados_bebidas = RecetaBebida.objects.filter(Q(nombre_receta__icontains=query))

        # Unir los resultados en una lista
        resultados = list(resultados_dulces) + list(resultados_saladas) + list(resultados_bebidas)

    context = {
        'resultados': resultados,  # Pasamos los resultados al template
    }

    return render(request, 'menu_principal.html', context)


# Vista para ingresar receta dulce
def ingresar_receta_dulce(request):
    if request.method == 'POST':
        form = RecetaDulceForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la receta en la base de datos
            return redirect('menu_principal')  # Redirige al menú principal después de guardar
    else:
        form = RecetaDulceForm()

    return render(request, 'ingresar_receta_dulce.html', {'form': form})


# Vista para ingresar receta salada
def ingresar_receta_salada(request):
    if request.method == 'POST':
        form = RecetaSaladaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la receta en la base de datos
            return redirect('menu_principal')  # Redirige al menú principal después de guardar
    else:
        form = RecetaSaladaForm()

    return render(request, 'ingresar_receta_salada.html', {'form': form})

# Vista para ingresar receta bebida
def ingresar_receta_bebida(request):
    if request.method == 'POST':
        form = RecetaBebidaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la receta en la base de datos
            return redirect('menu_principal')  # Redirige al menú principal después de guardar
    else:
        form = RecetaBebidaForm()

    return render(request, 'ingresar_receta_bebida.html', {'form': form})

# Vista para ingresar about
def about(request):
    return render(request, 'about.html')




