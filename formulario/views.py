from django.shortcuts import render
from .models import Usuario
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm


class UsuarioListView(ListView):
    model = Usuario
    template_name = "formulario/usuario_list.html"


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "formulario/usuario_form.html"
    success_url = reverse_lazy("usuario_list")
    extra_context = {"titulo": "Cadastre-se"}
