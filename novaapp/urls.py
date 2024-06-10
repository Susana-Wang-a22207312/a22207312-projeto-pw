from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view,name='index'),
    path('example/', views.example_view, name='example'),
    path('conclusion/', views.conclusion_view, name='conclusion'),
]