"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, aulas, cursos, administracao, infor, ven, tela_cadastro, enviar, detalhes_cursos
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('aulas/', aulas),
    path('cursos/', cursos),
    path("detalhes_cursos/<int:curso_id>/", views.curso_detalhe, name="curso_detalhe"),
    path('administracao/', administracao, name='administração'),
    path('infor/', infor),
    path('ven/', ven),
    path('enviar/', enviar),
    path('cadastro/', tela_cadastro , name= 'cadastro'),
]



