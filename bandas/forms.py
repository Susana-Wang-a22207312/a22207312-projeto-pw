from django import forms
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da Banda'}),
            'genero': forms.TextInput(attrs={'placeholder': 'Gênero Musical'}),
            'ano_formacao': forms.NumberInput(attrs={'placeholder': 'Ano de Formação'}),
            'pais_origem': forms.TextInput(attrs={'placeholder': 'País de Origem'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'titulo': 'Título',
            'gravadora': 'Gravadora',
        }
        help_texts = {
            'gravadora': 'Informe a gravadora do álbum',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do Álbum'}),
            'gravadora': forms.TextInput(attrs={'placeholder': 'Gravadora'}),
            'capa_album': forms.ClearableFileInput(attrs={'placeholder': 'Capa do Álbum'}),
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        labels = {
            'titulo': 'Título',
            'duracao': 'Duração (segundos)',
            'numero_faixa': 'Número da Faixa',
        }
        help_texts = {
            'duracao': 'Duração da música em segundos',
            'numero_faixa': 'Número da faixa no álbum',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título da Música'}),
            'duracao': forms.NumberInput(attrs={'placeholder': 'Duração em segundos'}),
            'numero_faixa': forms.NumberInput(attrs={'placeholder': 'Número da Faixa'}),
        }
