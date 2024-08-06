from django.urls import path
from NewApp import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar-formulario/', views.registrar_formulario, name='registrar_formulario'),
    path('fin/', views.fin, name='fin'), 
     path('buscar-empresas/', views.buscar_empresas, name='buscar_empresas'),
]