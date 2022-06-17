from django.contrib import admin
from django.contrib import admin

# Register your models here.
from .models import Balance, Insurance, Payment, Tax, Insurance, Balance

# # to show up in admin panel

class BalanceAdmin(admin.ModelAdmin):
    # gives the columns to be displayed in admin panel for Accounts
    list_display = ('account_id', 'payment_id', 'tax_id', 'insurance_id', 'discountbonus_id', 'directbonus', 'magicbonus', 'cash_in', 'cash_out', 'net_balance', 'narration')
    # list_display_links = ('email', 'first_name')
    # readonly_fields = ('last_login', 'date_joined')
    ordering = ('-created',)

    filter_horizontal = ()
    list_filter = ()
    # # makes password readonly fields
    # fieldsets = ()


admin.site.register(Payment)
admin.site.register(Tax)
admin.site.register(Insurance)
admin.site.register(Balance, BalanceAdmin)