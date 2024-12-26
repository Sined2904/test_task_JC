from django.shortcuts import render
from wallets.models import Wallet
from serializers import WalletSerializer, OperationWalletSerializer
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action


class WalletsViewSet(viewsets.ModelViewSet):
    '''Вьюсет для кошельков.'''

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer




class Operation(generics.CreateAPIView):
    
    queryset = Wallet.objects.all()
    serializer_class = OperationWalletSerializer


    def post(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        print(request)

        return super().post(request, *args, **kwargs)