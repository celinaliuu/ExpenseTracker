from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def addExpense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        # Expense.objects.create(expense)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            category = form.cleaned_data['category']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Expense.objects.create(amount=amount, category=category, date=date, description=description)

            return redirect('expenseLogs') # redirect to the expense logs
        else:
            form = ExpenseForm() # empty form for GET requests

        return render(request, 'addExpense.html', {'form': form})

def deleteExpense(request, expenseid):
    expense = Expense.objects.get(id = expenseid)
    expense.delete()
    return redirect('expenseLogs') # redirect to the expense logs

def expenseLogs(request):
    expenses = Expense.objects.all()
    return render(request, 'viewExpenses.html', {'expenses':expenses})

def updateView(request, expenseid): 
    expense = Expense.objects.get(pk = expenseid)
    return render(request, 'editExpense.html', {'expense':expense})

def updateExpense(request, expenseid):
     expense = Expense.objects.get(pk = expenseid)
     if request.method == 'POST':
        form = ExpenseForm(request.POST, instance = expense)
        # Expense.objects.create(expense)
        if form.is_valid():
            form.save()

            return redirect('expenseLogs') # redirect to the expense logs
        else:
            form = ExpenseForm() # empty form for GET requests

        return render(request, 'updateExpenseForm.html', {'form': form})