from django.db import models
from django.utils.timezone import now

ROLE_CHOICES = (
    ('1', 'admin'),
    ('2', 'user'),
    ('3', 'store_owner'),
)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Store(models.Model):
    class Industry(models.TextChoices):
        FOOD_BEVERAGE = 'F&B'
        E_COMMERCE = 'E-Commerce'
        ADVERTISEMENT = 'Advertisement'

    store_name = models.CharField(max_length=100, verbose_name='Store Name')
    store_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    logo = models.ImageField(upload_to='store/logo', blank=True)
    industry = models.CharField(max_length=100, choices=Industry.choices)
    website = models.CharField(max_length=100, blank=True)
    bank = models.CharField(max_length=50, blank=True)
    account_number = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return f'{self.store_name}'

class Payout(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default="")
    date = models.DateField(default=now)
    status = models.CharField(max_length=20, blank=True, null=True)
    amount = models.BigIntegerField()

    def store_bank(self):
        return f'{self.store.bank}'