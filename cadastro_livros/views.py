# Create your views here.
from .models import Livro
from django.shortcuts import render
from .serializers import LivroSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView, 
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView
)

# Create your views here.

class LivroListView(ListView):
    model = Livro


class LivroDetailView(DetailView):
    model = Livro
    
class LivroViewSet(ModelViewSet):
    serializer_class = LivroSerializer
    queryset = Livro.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class LivroCreateView(LoginRequiredMixin, CreateView):
    model = Livro
    fields = [
        'titulo',
        'autor',
        'data_de_lancamento',
        'estado',
        'paginas',
        'empresa_publicadora'
    ]

    # def form_valid(self, form):
    #     form.instance.autor = self.request.user
    #     return super().form_valid(form)


class LivroUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Livro
    fields = [
        'titulo',
        'autor',
        'isbn',
        'data_de_lancamento',
        'estado',
        'paginas',
        'empresa_publicadora',
        'capa',
        'pdf'
    ]

    # def form_valid(self, form):
    #     form.instance.autor = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     livro = self.get_object()
    #     if self.request.user == livro.autor:
    #         return True
    #     elif self.request.user != livro.autor:
    #         if str(self.request.user) == 'admin':
    #             return True
    #     return False


class LivroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Livro
    success_url = '/'

    # def test_func(self):
    #     livro = self.get_object()
    #     if self.request.user == livro.autor:
    #         return True
    #     if self.request.user != livro.autor:
    #         if str(self.request.user) == 'admin':
    #             return True
    #     return False