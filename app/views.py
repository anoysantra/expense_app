from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExpenseForm , MonthForm, CategoryMonthForm
from .models import Expense
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from collections import defaultdict

def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  
  # Redirect to the list of expenses after saving
    else:
        form = ExpenseForm()
    return render(request, 'expense_form.html', {'form': form})


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})



def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():  

            form.save()
            return redirect('expense_by_month')  # Redirect to  the list of expenses after updating
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_form.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_by_month')  # Redirect to the list of expenses after deleting
    return render(request, 'expense_confirm_delete.html', {'expense': expense})


#month-wise expenses

def expense_by_month(request):
    form = MonthForm(request.POST or None)
    if form.is_valid():
        month = form.cleaned_data['month']
        expenses = Expense.objects.filter(date__month=month)
        total_expenses = expenses.count()
        total_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        return render(request, 'expense_by_month.html', {
            'form': form,
            'expenses': expenses,
            'total_expenses': total_expenses,
            'total_amount': total_amount,
            'month': month,
        })
    return render(request, 'expense_by_month.html', {'form': form})


def expense_category(request):
    form = CategoryMonthForm(request.POST or None)
    total_amount = 0
    expenses = None

    if request.method == 'POST' and form.is_valid():
        month = form.cleaned_data['month']
        category = form.cleaned_data['category']
        
        # Filtering expenses based on month and category
        expenses = Expense.objects.filter(date__month=month, category=category)
        
        # Calculating the total amount for the filtered expenses
        total_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'expense_by_category.html', {
        'form': form,
        'expenses': expenses,
        'total_amount': total_amount,
    })
