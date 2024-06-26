from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

#Aparecer campo filmes_vistos no admin
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Informações pessoais", {"fields": ('filmes_vistos ',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)