from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Digite sua senha"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Digite seu E-Mail"})
    )

    class Meta:
        model = Usuario
        fields = ["nome", "email", "data_de_nascimento", "senha"]
        widgets = {"data_de_nascimento": forms.DateInput(attrs={"type": "date"})}

