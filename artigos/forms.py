from django import forms
from .models import *


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ["texto", "fotografia", "link_externo"]


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]