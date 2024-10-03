from django.urls import path
from .views import *

urlpatterns = [
    path('Index', IndexView.as_view(), name='index'),
    path('Viagem', ViagemView.as_view(), name='viagem'),
    path('Reserva', ReservaView.as_view(), name='reserva'),
    path('Avaliacai', AvaliacaoView.as_view(), name='reserva'),
    path('UsuarioPerfil', UsuarioPerfilView.as_view(), name='usuarioPerfil'),
]


  
    
    