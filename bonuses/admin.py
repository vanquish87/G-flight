from django.contrib import admin

# Register your models here.
from .models import DiscountBonus, DirectBonus, LeadershipBonus, MagicBonus

# # to show up in admin panel
admin.site.register(DiscountBonus)
admin.site.register(DirectBonus)
admin.site.register(MagicBonus)
admin.site.register(LeadershipBonus)