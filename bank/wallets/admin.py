from django.contrib import admin
from models import Wallet


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'ballance')
    search_fields = ('id', 'ballance')
    list_filter = ('id', 'ballance')
    empty_value_display = '-пусто-'
    ordering = ['id']

admin.site.register(Wallet, WalletAdmin)