from django import forms

class ExpenseForm (forms.Form): 
    amount = forms.DecimalField(decimal_places=2, max_digits=10)
    category = forms.CharField(max_length=200)
    date = forms.DateField()
    description = forms.CharField(max_length=200)