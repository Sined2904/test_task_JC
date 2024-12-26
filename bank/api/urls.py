from django.urls import path

from .views import WalletRetrieveView, OperationView


app_name = 'api'

urlpatterns = [
    path(
    'wallets/<int:pk>',
    WalletRetrieveView.as_view(),
    name='list'),
    path(
    'wallets/<int:pk>/operation',
    OperationView.as_view(),
    name='operation'),

]
