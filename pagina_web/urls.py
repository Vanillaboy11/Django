#pagina_web/urls.py
from django.urls import path
from .views import vistaPaginaDeInicio

urlpatterns = [
    path('', vistaPaginaDeInicio, name='paginaInicio')
]