from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense (models.Model): 
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.TextField(max_length=200)
    date = models.DateField()
    description = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_data', null=True)
    
