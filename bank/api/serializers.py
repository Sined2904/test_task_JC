import base64
import re

from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.core.files.base import ContentFile
from dotenv import load_dotenv
import os

load_dotenv()
from wallets.models import Wallet


ALLOWED_OPERATION = os.getenv('ALLOWED_OPERATION', '').split(',')


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