from django.contrib import admin

from .models import AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente, Curso

@admin.register(AreaCientifica)
class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano', 'semestre', 'ects', 'curricularUnitReadableCode', 'area_cientifica']

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'conceitos_aplicados', 'tecnologias_usadas', 'imagem', 'video_demo', 'github_repo', 'disciplina']

@admin.register(LinguagemProgramacao)
class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['apresentacao', 'objetivos', 'competencias']

