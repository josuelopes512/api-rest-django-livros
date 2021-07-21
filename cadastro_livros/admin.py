from .models import Livro
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.

@admin.register(Livro)
class LivroAdmin(ModelAdmin):
    # list_display = ("title", "slug", "author", "created", "updated")
    list_display = (
        'titulo',
        'autor',
        'data_de_lancamento',
        'estado',
        'paginas',
        'empresa_publicadora',
        "updated_at"
    )
    prepopulated_fields = {"slug": ("titulo",)}