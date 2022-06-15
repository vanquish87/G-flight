from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

import uuid

# Create your models here.
# Creating model where email becomes username
class MyAccountManager(BaseUserManager):
    # creating normal user
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email.')

        # to get email in smallcaps used normalize_email
        user = self.model(email=self.normalize_email(email))

        # use inbuild function to set password maybe gonna hash the original
        user.set_password(password)
        user.save(using=self._db)
        return user

    # creating admin
    def create_superuser(self, email, password):
        # using create_user function defined above
        user = self.create_user(email=self.normalize_email(email), password=password)

        # giving permissions
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)

class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(max_length=16, unique=True, blank=True, null=True)

    # required
    # create Timestamp automatically
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # login with email
    USERNAME_FIELD = 'email'
    # we only require email in starting. so leaving others
    # REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

# Every Account will be isssued with unique referral code which can be shared multiple times
class Referral(models.Model):
    # on_delete will decide if original Key ie, Account is deleted what will happen in this model, CASCADE will delete all the Referral
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    # unique code 
    code = models.CharField(max_length=80)
    # jisse invitation mila tha uska code
    invited_from = models.CharField(max_length=80) 
    # how many times Referral code is used, to be used in conjuctiion with LeadershipBonus
    used = models.IntegerField(default=0)

    # create Timestamp automatically
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    
    # this is what you get when object is instantiated of this class
    # for ex: in Admin Panel
    def __str__(self):
        return self.code