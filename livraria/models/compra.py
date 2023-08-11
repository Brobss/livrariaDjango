from django.db import models

from .livro import Livro
from usuario.models import Usuario


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = (
            1,
            "Carrinho",
        )
        REALIZADO = (
            2,
            "Realizado",
        )
        PAGO = (
            3,
            "Pago",
        )
        ENTREGUE = (
            4,
            "Entregue",
        )

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    quantidade = models.IntegerField(default=1)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=1, choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

    def __str__(self):
        return self.livro.titulo
