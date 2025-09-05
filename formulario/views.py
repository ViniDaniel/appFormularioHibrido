from .models import Usuario
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.views.generic import DetailView

class UsuarioSuccessView(DetailView):
    model = Usuario
    template_name = "formulario/usuario_sucesso.html"
    context_object_name = "usuario"

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "formulario/usuario_form.html"
    extra_context = {"titulo": "Cadastre-se"}

    def get_success_url(self):
        return reverse_lazy("usuario_sucesso", kwargs={"pk": self.object.pk})
