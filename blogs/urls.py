from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'blogs'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('artigo/<str:artigo_nome>/', views.artigo_view, name='artigo'),
    path('autor/<str:autor_nome>/', views.autor_view, name='autor'),
    path('novo_artigo/', views.novo_artigo_view, name='novo_artigo'),
    path('edita_artigo/<int:artigo_id>/', views.edita_artigo_view, name='edita_artigo'),
    path('apaga_artigo/<int:artigo_id>/', views.apaga_artigo_view, name='apaga_artigo'),
    path('novo_autor/', views.novo_autor_view, name='novo_autor'),
    path('edita_autor/<int:autor_id>/', views.edita_autor_view, name='edita_autor'),
    path('apaga_autor/<int:autor_id>/', views.apaga_autor_view, name='apaga_autor'),
    path('novo_comentario/<int:artigo_id>/', views.novo_comentario_view, name='novo_comentario'),
    path('edita_comentario/<int:comentario_id>/', views.edita_comentario_view, name='edita_comentario'),
    path('apaga_comentario/<int:comentario_id>/', views.apaga_comentario_view, name='apaga_comentario'),
    path('novo_rating/<int:artigo_id>/', views.novo_rating_view, name='novo_rating'),
    path('edita_rating/<int:rating_id>/', views.edita_rating_view, name='edita_rating'),
    path('apaga_rating/<int:rating_id>/', views.apaga_rating_view, name='apaga_rating'),
]