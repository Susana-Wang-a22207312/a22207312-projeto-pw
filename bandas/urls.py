from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name="bandas"),
    path('bandas/<int:banda_id>', views.bandas_view,name='banda'),
    path('album/<str:album_nome>', views.album_view, name='album'),
    path('musica/<str:musica_nome>', views.musica_view, name='musica'),
    path('membro/<str:membro_nome>', views.membro_view, name='membro'),

    path('banda/nova/', views.nova_banda_view, name='nova_banda'),
    path('banda/edita/<int:banda_id>/', views.edita_banda_view, name='edita_banda'),
    path('banda/apaga/<int:banda_id>/', views.apaga_banda_view, name='apaga_banda'),


    path('album/novo/<int:banda_id>/', views.novo_album_view, name='novo_album'),
    path('album/edita/<int:album_id>/', views.edita_album_view, name='edita_album'),
    path('album/apaga/<int:album_id>/', views.apaga_album_view, name='apaga_album'),


    path('musica/novo/<int:album_id>/', views.nova_musica_view, name='nova_musica'),
    path('musica/edita/<int:musica_id>/', views.edita_musica_view, name='edita_musica'),
    path('musica/apaga/<int:musica_id>/', views.apaga_musica_view, name='apaga_musica'),
]