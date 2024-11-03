from django import forms
from .models import Expense

class ExpenseForm (forms.ModelForm): 
    # amount = forms.DecimalField(decimal_places=2, max_digits=10)
    # category = forms.CharField(max_length=200)
    # date = forms.DateField()
    # description = forms.CharField(max_length=200)
    class Meta: 
        model = Expense
        fields = ["amount", "category", "date", "description"]