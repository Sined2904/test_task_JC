from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import WalletsViewSet, Operation


app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('wallets', WalletsViewSet, basename='tags')


urlpatterns = [
    path('', include(router_v1.urls)),
    path(
    'wallets/<int:recipe_id>/operation',
    Operation.as_view(),
    name='operation'),

]
