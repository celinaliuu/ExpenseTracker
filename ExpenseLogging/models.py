from django.db import models

# Create your models here.
class Expense (models.Model): 
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.TextField(max_length=200)
    date = models.DateField()
    description = models.TextField(max_length=200)
