from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.index_view, name="cursos"),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina'),
    path('projeto/<int:projeto_id>/', views.projeto_view, name='projeto'),
    path('docente/<int:docente_id>/', views.docente_view, name='docente'),

    path('nova-disciplina/', views.nova_disciplina_view, name='nova_disciplina'),
    path('disciplina/<int:disciplina_id>/novo_projeto/', views.novo_projeto_view, name='novo_projeto'),
    path('disciplina/<int:disciplina_id>/novo-docente/', views.novo_docente_view, name='novo_docente'),

    path('edita-disciplina/<int:disciplina_id>/', views.edita_disciplina_view, name='edita_disciplina'),
    path('edita-projeto/<int:projeto_id>/', views.edita_projeto_view, name='edita_projeto'),
    path('edita-docente/<int:docente_id>/', views.edita_docente_view, name='edita_docente'),

    path('apaga-disciplina/<int:disciplina_id>/', views.apaga_disciplina_view, name='apaga_disciplina'),
    path('apaga-projeto/<int:projeto_id>/', views.apaga_projeto_view, name='apaga_projeto'),
    path('apaga-docente/<int:docente_id>/', views.apaga_docente_view, name='apaga_docente'),
]
