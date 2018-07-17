from django.contrib import admin

# Register your models here.
from pwdj.galeria.models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = 'titulo preco'.split()
    ordering = ('titulo',)
