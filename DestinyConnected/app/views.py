from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

class HomePageView(View):
    template_name = 'home.html'  
    def get(self, request):
        return render(request, self.template_name)

class ViagemView(View):
    def get(self, request):
        viagem = Viagem.objects.all()
        return render(request, 'index.html', {'viagem': viagem})
        def post(self, request):
            pass

class ReservaView(View):
    def get(self, request):
        reserva = Reserva.objects.all()
        return render(request, 'viagem.html', {'reserva': reserva})
        def post(self, request):
            pass

class AvaliacaoView(View):
    def get(self, request):
        avaliacao = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacao': avaliacao})
        def post(self, request):
            pass

class UsuarioPerfilView(View):
    def get(self, request):
        usuarioPerfil = UsuarioPerfil.objects.all()
        return render(request, 'usuarioPerfil.html', {'usuarioPerfil': usuarioPerfil})
        def post(self, request):
            pass