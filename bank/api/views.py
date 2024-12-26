import os

from django.shortcuts import get_object_or_404
from dotenv import load_dotenv
from rest_framework import generics, status
from rest_framework.response import Response
from wallets.models import Wallet

from .serializers import OperationWalletSerializer, WalletSerializer

load_dotenv()

OPERATIONS_OF_DEPOSIT = os.getenv('OPERATIONS_OF_DEPOSIT', '').split(',')
OPERATIONS_OF_WITHDRAW = os.getenv('OPERATIONS_OF_WITHDRAW', '').split(',')


class WalletRetrieveView(generics.RetrieveAPIView):
    """Вью для отображения баланса кошелька."""

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class OperationView(generics.CreateAPIView):
    """Вью для пополнения и снятия."""

    queryset = Wallet.objects.all()
    serializer_class = OperationWalletSerializer

    def post(self, request, *args, **kwargs):
        wallet = get_object_or_404(Wallet, id=self.kwargs['pk'])
        amount = round(float(request.data['amount']), 2)
        if amount < 0:
            return Response(f'Сумма должна быть больше 0!', status=status.HTTP_200_OK)
        if request.data['operationType'] in OPERATIONS_OF_DEPOSIT:
            new_balance = wallet.balance + amount
            wallet.balance = new_balance
            wallet.save()
            return Response(f'Вы внесли {amount}!', status=status.HTTP_200_OK)
        if request.data['operationType'] in OPERATIONS_OF_WITHDRAW:
            new_balance = wallet.balance - amount
            if new_balance <0:
                return Response('Недостаточно средств для снятия', status=status.HTTP_200_OK)
            else:
                wallet.balance = new_balance
                wallet.save()
            return Response(f'Вы сняли {amount}!', status=status.HTTP_200_OK)
        return Response('Неизвестный тип операции', status=status.HTTP_200_OK)