from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class ViagemView(View):
    template_name = 'viagem.html'
    def get(self, request):
        viagens = Viagem.objects.all()
        return render(request, self.template_name, {'viagens': viagens})
        def post(self, request):
                pass

class ReservaView(View):
    template_name = 'reserva.html'

    def get(self, request):
         reservas = Reserva.objects.all()
         return render(request, self.template_name, {'reservas': reservas})
    def post(self, request):
        pass
class AvaliacaoView(View):
    def get(self, request):
        avaliacao = Avaliacao.objects.all()
        viagens = Viagem.objects.all()  
        return render(request, 'avaliacao.html', {'avaliacao': avaliacao, 'viagens': viagens})
    def post(self, request):
        pass


class UsuarioPerfilView(View):
    template_name = 'usuario.html'

    def get(self, request):
        usuario_perfis = UsuarioPerfil.objects.all()
        return render(request, self.template_name, {'usuario': usuario_perfis})

    def post(self, request):
        pass

class CadastroView(View):
    template_name = 'cadastro.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass