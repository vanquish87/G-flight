from django.db import models
import uuid

from accounts.models import Account
from bonuses.models import DirectBonus, DiscountBonus, MagicBonus

# Create your models here.
class Payment(models.Model):
    # one to many with Account, on_delete it will remain 
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL)
    # inward amount from payment gateway
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    # from payment gateway
    payment_num = models.CharField(max_length=200, unique=True)
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
        ('GST', 'GST'),
        ('TDS', 'TDS')
    )
    type = models.CharField(max_length=200, choices=TAX_TYPE)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    # OneToOne relatioship
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    payment = models.OneToOneField(Payment, on_delete=models.RESTRICT)
    
    # to='bonuses.DirectBonus' used to avoid Circular (or cyclic) imports
    # solve 'It is impossible to add a non-nullable field 'directbonus' to tax without specifying a default' added null=True
    directbonus = models.OneToOneField(to='bonuses.DirectBonus', on_delete=models.RESTRICT, null=True)

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


class Insurance(models.Model):
    # one to many with Account, on_delete it will remain 
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL)
    # OneToOne relatioship
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    payment = models.OneToOneField(Payment, on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    issue_num = models.CharField(max_length=200, unique=True)

    # create Timestamp automatically
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.issue_num

# it will have everything connected & will look like bank statement
class Balance(models.Model):
    # one to many with Account, on_delete it will remain 
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL)
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    payment = models.OneToOneField(Payment, on_delete=models.RESTRICT, null=True)
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    tax = models.OneToOneField(Tax, on_delete=models.RESTRICT, null=True)
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    insurance = models.OneToOneField(Insurance, on_delete=models.RESTRICT, null=True)
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    discountbonus = models.OneToOneField(DiscountBonus, on_delete=models.RESTRICT, null=True)
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    directbonus = models.OneToOneField(DirectBonus, on_delete=models.RESTRICT, null=True)
    # To delete it you will have to delete all objects that reference it manually. RESTRICT
    magicbonus = models.OneToOneField(MagicBonus, on_delete=models.RESTRICT, null=True)
    
    cash_in = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    cash_out = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    # solve 'It is impossible to add a non-nullable field 'directbonus' to tax without specifying a default' added null=True
    net_balance = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    
    # create Timestamp automatically
    created = models.DateTimeField(auto_now_add=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    