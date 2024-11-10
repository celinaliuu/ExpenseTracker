from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm (UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
    def save(self, commit = True):
        user = super(SignUpForm, self).save(commit = False)
        if commit:
            user.save()
        return user

class ExpenseForm (forms.ModelForm): 
    # amount = forms.DecimalField(decimal_places=2, max_digits=10)
    # category = forms.CharField(max_length=200)
    # date = forms.DateField()
    # description = forms.CharField(max_length=200)
    class Meta: 
        model = Expense
        fields = ["amount", "category", "date", "description"]


