from django.test import TestCase, Client
from wallets.models import Wallet
import json


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()
        Wallet.objects.create(balance = 100)

    def test_of_available_get_wallets(self):
        """Проверка доступности адреса /api/v1/wallets/1."""

        response = self.guest_client.get('/api/v1/wallets/1')
        self.assertEqual(response.status_code, 200)

    def test_of_available_post_deposit_wallets(self):
        """Проверка пополнения кошелька api/v1/wallets/1/operation."""
        wallet = Wallet.objects.get(id=1)
        response = self.guest_client.post('/api/v1/wallets/1/operation', {"operationType": "DEPOSIT", "amount": 10})
        new_wallet = Wallet.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(wallet.balance+10, new_wallet.balance)

    def test_of_available_post_withdraw_wallets(self):
        """Проверка списания с кошелька api/v1/wallets/1/operation."""

        wallet = Wallet.objects.get(id=1)
        response = self.guest_client.post('/api/v1/wallets/1/operation', {"operationType": "WITHDRAW", "amount": 10})
        new_wallet = Wallet.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(wallet.balance-10, new_wallet.balance)