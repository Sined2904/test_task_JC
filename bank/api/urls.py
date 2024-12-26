from django.urls import include, path
from rest_framework.routers import DefaultRouter

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
