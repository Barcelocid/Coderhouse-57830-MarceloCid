from django.urls import path
from .views import register_view, login_view, logout_view, menu_principal, ingresar_receta_dulce, ingresar_receta_salada, ingresar_receta_bebida, about


urlpatterns = [
    path('register/', register_view, name='register'), # Ruta para registrar usuario
    path('login/', login_view, name='login'), # Ruta para hacer login
    path('logout/', logout_view, name='logout'),  # Ruta para cerrar sesión
    path('menu/', menu_principal, name='menu_principal'),  # Ruta para el menú principal
    path('buscar/', menu_principal, name='buscar_receta'),  # Ruta para buscar recetas
    path('receta-dulce/', ingresar_receta_dulce, name='ingresar_receta_dulce'), # Ruta para receta dulce
    path('receta-salada/', ingresar_receta_salada, name='ingresar_receta_salada'), # Ruta para receta salada
    path('receta-bebida/', ingresar_receta_bebida, name='ingresar_receta_bebida'), # Ruta receta bebida
    path('about/', about, name='about'), # Ruta para el about

]

