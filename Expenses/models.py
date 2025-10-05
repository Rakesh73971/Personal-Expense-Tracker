from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Expense(models.Model):
    PAYMENT_CASH = 'Cash'
    PAYMENT_CARD = 'Card'
    PAYMENT_UPI = 'UPI'
    PAYMENT_BANK = 'Bank Transfer'
    PAYMENT_CHOICES = [
        (PAYMENT_CASH,'Cash'),
        (PAYMENT_CARD,'Card'),
        (PAYMENT_UPI,'UPI'),
        (PAYMENT_BANK,'Bank Transfer')
    ]
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    title = models.CharField(max_length=255)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places = 2,
        validators=[MinValueValidator(0.01)]
    )
    note = models.TextField(null=True,blank=True)
    date = models.DateField(default=timezone.now().date())
    payment_method = models.CharField(max_length=20,choices=PAYMENT_CHOICES,default=PAYMENT_CASH)

    def __str__(self):
        return f"{self.title},{self.amount}"
