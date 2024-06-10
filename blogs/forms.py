from django import forms
from .models import Autor, Artigo, Comentario, Rating

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'bio']

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor_nome', 'texto']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['autor_nome', 'rating']
