from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('mebyme/', views.me_by_me, name='me_by_me'),
    path('categories/', views.categories, name='categories'),
    path('bestSellers/', views.best_sellers, name='best_sellers'),
    path('contact/', views.contact, name='contact'),
    path('1stYear/', views.ano1_de_LEI, name='1st_year'),
    path('2ndYear/', views.ano2_de_LEI, name='2nd_year'),
    path('3rdYear/', views.ano3_de_LEI, name='3rd_year'),
    path('skills/', views.skills, name='skills'),
    path('videos/', views.videos, name='videos'),
]
