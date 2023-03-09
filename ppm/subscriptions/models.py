from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from djstripe.models import Customer, Plan


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    subscription_plan = models.ForeignKey(Plan, on_delete=models.CASCADE)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.email

    def get_short_name(self):
        return self.email


class FreeUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='free_user')
    is_active = models.BooleanField(default=True)


class PaidUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='paid_user')
    is_active = models.BooleanField(default=True)
    subscription_plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    next_payment_date = models.DateField(null=True)


class CorporateAccount(models.Model):
    name = models.CharField(max_length=100)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='corporate_account')
    is_active = models.BooleanField(default=True)
    subscription_plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    next_payment_date = models.DateField(null=True)
    users = models.ManyToManyField(CustomUser, related_name='corporate_accounts')
