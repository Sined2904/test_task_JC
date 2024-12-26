from django.db import models

class Wallet(models.Model):
    """Модель кошелька."""

    balance = models.FloatField('Баланс кошелька')

    def deposit(self, amount):
        if amount <= 0:
            self.balance += amount
            return self.balance
        else:
            return 'Сумма пополнения должна быть больше или равно 0'

    def withdraw(self, amount):
        if amount <= 0:
            self.balance -= amount
            return self.balance
        else:
            return 'Сумма списания должна быть больше или равно 0'

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return f'Баланс {self.id} - {self.balance}'