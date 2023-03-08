from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

'''
SubscriptionPlan: represents a subscription plan with a name, price, maximum number of users, description, and active status.
Company: represents a company with a name, address, city, country, and associated subscription plan.
CustomUser: represents a user with an email, associated company, name, and other attributes. This model extends AbstractBaseUser but does not include any subscription-specific fields.
FreeUser: represents a user with a free subscription. This model
'''


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    max_users = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)


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
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    subscription_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

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
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    next_payment_date = models.DateField(null=True)


class CorporateAccount(models.Model):
    name = models.CharField(max_length=100)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='corporate_account')
    is_active = models.BooleanField(default=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    next_payment_date = models.DateField(null=True)
    users = models.ManyToManyField(CustomUser, related_name='corporate_accounts')
