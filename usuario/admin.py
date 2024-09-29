from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import PerfilUsuario, RecetaDulce, RecetaBebida, RecetaSalada  # Importa tu modelo de perfil de usuario



# Registrar el perfil de usuario en el admin
class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario  # El modelo de perfil que contiene información extra
    can_delete = False
    verbose_name_plural = 'Perfiles de Usuarios'

# Extendemos la clase del admin de usuarios de Django para incluir el perfil de usuario
class UsuarioAdmin(UserAdmin):
    inlines = (PerfilUsuarioInline,)  # Agregamos el perfil como una sección dentro del usuario

# Volvemos a registrar el modelo de usuario con la clase UsuarioAdmin
admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)


# Registramos el modelo RecetaDulce en el admin
class RecetaDulceAdmin(admin.ModelAdmin):
    list_display = ('nombre_receta', 'nombre_persona', 'fecha_subida', 'edad')

admin.site.register(RecetaDulce, RecetaDulceAdmin)

# Registramos el modelo RecetaSalada en el admin
class RecetaSaladaAdmin(admin.ModelAdmin):
    list_display = ('nombre_receta', 'nombre_persona', 'fecha_subida', 'edad')

admin.site.register(RecetaSalada, RecetaSaladaAdmin)

# Registramos el modelo RecetaBebida en el admin
class RecetaBebidaAdmin(admin.ModelAdmin):
    list_display = ('nombre_receta', 'nombre_persona', 'fecha_subida', 'edad')

admin.site.register(RecetaBebida, RecetaBebidaAdmin)
