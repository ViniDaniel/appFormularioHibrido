

from django.contrib import admin
from django.urls import path
from formulario.views import (
    UsuarioCreateView,
    UsuarioSuccessView
)

urlpatterns = [
    path("", UsuarioCreateView.as_view(), name="usuario_form"),
    path("sucesso/<int:pk>/", UsuarioSuccessView.as_view(), name="usuario_sucesso"),
]
