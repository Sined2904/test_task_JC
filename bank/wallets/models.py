from django.db import models


class Wallet(models.Model):
    """Модель кошелька."""

    balance = models.FloatField('Баланс кошелька')

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return f'Баланс кошелька №{self.id} - {self.balance}'