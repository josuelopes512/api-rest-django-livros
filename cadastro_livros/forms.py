from .models import Livro
from django.forms import  ModelForm

class LivroModelForm(ModelForm):
    class Meta:
        model = Livro
        fields = [
            "titulo", 
            "autor", 
            "isbn", 
            "data_de_lancamento", 
            'paginas', 
            "estado", 
            "empresa_publicadora", 
            "capa", 
            'pdf'
]