from django.contrib import admin

from .models import Wallet


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance')
    search_fields = ('id', 'balance')
    list_filter = ('id', 'balance')
    empty_value_display = '-пусто-'
    ordering = ['id']

admin.site.register(Wallet, WalletAdmin)
