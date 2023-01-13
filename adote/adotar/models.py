from django.db import models
from django.contrib.auth.models import User
from adote.divulgar.models import Pet

# Create your models here.
class PedidoAdocao(models.Model):
    choices_status = (
        ('AG', 'Aguardando aprovação'),
        ('AP', 'Aprovado'),
        ('R', 'Recusado')
    )

    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    status = models.CharField(max_length=2, choices=choices_status, default='AG')

    def __str__(self) -> str:
        return self.pet.nome