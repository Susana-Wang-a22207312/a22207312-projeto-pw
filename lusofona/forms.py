from django import forms
from .models import AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente, Curso

class AreaCientificaForm(forms.ModelForm):
    class Meta:
        model = AreaCientifica
        fields = ['nome']

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'ano', 'semestre', 'ects', 'curricularUnitReadableCode', 'area_cientifica']

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['descricao', 'conceitos_aplicados', 'tecnologias_usadas', 'imagem', 'video_demo', 'github_repo', 'disciplina']

class LinguagemProgramacaoForm(forms.ModelForm):
    class Meta:
        model = LinguagemProgramacao
        fields = ['nome']

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nome', 'disciplinas']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['apresentacao', 'objetivos', 'competencias', 'disciplinas']
