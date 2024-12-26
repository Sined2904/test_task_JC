from rest_framework import serializers

from wallets.models import Wallet


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('id', 'balance')


class OperationWalletSerializer(serializers.ModelSerializer):
    
    operationType = serializers.CharField()
    amount = serializers.FloatField()
    class Meta:
        model = Wallet
        fields = ('amount', 'operationType')