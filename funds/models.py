from tabnanny import verbose
from django.db import models
import uuid

from accounts.models import Account

# Create your models here.
class Payment(models.Model):
    # one to many with Account, on_delete it will remain 
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL)
    # inward amount from payment gateway
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    # from payment gateway
    payment_number = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=False)
    
    # create Timestamp automatically
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    # this is what you get when object is instantiated of this class
    # for ex: in Admin Panel
    def __str__(self):
        return self.payment_id

    
class Tax(models.Model):
    # creating tuple for value that will be prefilled
    TAX_TYPE = ( 
        ('GST', 'Goods n Services Tax'),
        ('TDS', 'Tax Deducted at Source')
    )
    # OneToOne relatioship
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    payment = models.OneToOneField(Payment, on_delete=models.RESTRICT)

    type = models.CharField(max_length=200, choices=TAX_TYPE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    # directbonus =
    
    # create Timestamp automatically
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # to get right name in admin panel
    class Meta:
        verbose_name = 'tax'
        verbose_name_plural = 'taxes'

    def __str__(self):
        return self.type
