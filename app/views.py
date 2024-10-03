from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

class IndexView(View):
    template_name = 'index.html'  
    def get(self, request):
        return render(request, self.template_name)

class ViagemView(View):
   def viagens_disponiveis_view(request):
        viagens = Viagem.objects.all()
        return render(request, 'viagens_disponiveis.html', {'viagens': viagens})
        def post(self, request):
                pass

class ReservaView(View):
    def reserva_view(request):
        reservas = Reserva.objects.all()
        return render(request, 'reservas.html', {'reservas': reservas})
        def post(self, request):
            pass
class AvaliacaoView(View):
    def get(request):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})
        def post(self, request):
            pass

class UsuarioPerfilView(View):
        def perfil_usuario_view(request):
            usuario_perfis = UsuarioPerfil.objects.all()
            return render(request, 'perfil_usuario.html', {'usuario_perfis': usuario_perfis})
            def post(self, request):
                pass