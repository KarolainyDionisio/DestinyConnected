from django.urls import path
from .views import HomePageView, ViagemView, ReservaView, AvaliacaoView, UsuarioPerfilView

urlpatterns = [
     path('', HomePageView.as_view(), name='home'),
    path('Index', ViagemView.as_view(), name='index'),
    path('Reserva', ReservaView.as_view(), name='reserva'),
    path('Avaliacao', AvaliacaoView.as_view(), name='avaliacao'),
    path('UsuarioPerfil', UsuarioPerfilView.as_view(), name='usuarioPerfil'),
]


  
    
    