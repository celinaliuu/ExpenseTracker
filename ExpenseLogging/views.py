from django.shortcuts import render
from .models import Expense

# Create your views here.
def addExpense(request):
    if request.method == 'POST':
        expense = request.POST['expense']
        Expense.objects.create(expense)

def deleteExpense(request, expenseid):
    expense = Expense.objects.get(id = expenseid)
    expense.delete()

def expenseLogs(request):
    expenses = Expense.objects.all()
    return render(request, 'viewExpenses.html', {'expenses':expenses})