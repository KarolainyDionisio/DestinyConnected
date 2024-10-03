from django.db import models
from django.contrib.auth.models import User

class Viagem(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_viagem = models.DateField()
    hora_saida = models.TimeField()
    motorista = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viagens')
    vagas_disponiveis = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origem} para {self.destino} - {self.data_viagem}"

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name='reservas')
    num_passageiros = models.PositiveIntegerField()

    def __str__(self):
        return f"Reserva de {self.usuario.username} para {self.viagem}"

class Avaliacao(models.Model):
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Nota de 1 a 5
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Avaliação de {self.usuario.username} para {self.viagem} - Nota: {self.nota}"

class UsuarioPerfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return self.usuario.username
