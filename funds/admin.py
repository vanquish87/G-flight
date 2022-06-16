from django.contrib import admin

# Register your models here.
from .models import Balance, Insurance, Payment, Tax, Insurance, Balance

# # to show up in admin panel
admin.site.register(Payment)
admin.site.register(Tax)
admin.site.register(Insurance)
admin.site.register(Balance)