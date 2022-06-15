from django.contrib import admin

# Register your models here.
from .models import Payment, Tax

# # to show up in admin panel
admin.site.register(Payment)
admin.site.register(Tax)