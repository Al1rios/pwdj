from django.contrib import admin

# Register your models here.
from pwdj.galeria.models import Model, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    ordering = ('titulo',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = 'categoria titulo preco criacao ultima_alteracao'.split()
    ordering = ('categoria', 'titulo',)
