from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def customLogout(request):
    logout(request)
    return redirect('expenseLogs')

def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('expenseLogs')
        else:
            messages.error(request, 'sign up failed')

    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {'form': form})


@login_required
def addExpense(request):
    user = request.user
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        # Expense.objects.create(expense)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            category = form.cleaned_data['category']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Expense.objects.create(amount=amount, category=category, date=date, description=description, user=user)

            return redirect('expenseLogs') # redirect to the expense logs
        else:
            form = ExpenseForm() # empty form for GET requests

        return render(request, 'addExpense.html', {'form': form})
        # expenses = Expense.objects.filter(user=user)
        # return render(request, 'viewExpenses.html', {'form': form, 'expenses': expenses})
    
@login_required
def deleteExpense(request, expenseid):
    expense = Expense.objects.get(id = expenseid)
    expense.delete()
    return redirect('expenseLogs') # redirect to the expense logs

@login_required
def expenseLogs(request):
    user = request.user
    expenses = Expense.objects.filter(user=user).values()
    return render(request, 'viewExpenses.html', {'expenses':expenses})

@login_required
def updateView(request, expenseid): 
    expense = Expense.objects.get(pk = expenseid)
    formatteddate = expense.date.strftime('%Y-%m-%d')
    return render(request, 'editExpense.html', {'expense':expense, 'formatteddate' : formatteddate})

# def addExpenseView(request):
#     if request.method == "POST":
#         pass
#     return render(request, 'addExpense.html')

@login_required
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