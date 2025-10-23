from django.db.models import Sum, Case, When, DecimalField
from django.shortcuts import render, redirect, get_object_or_404
from .models import Entries
from .forms import EntryForm

def dashboard(request):
    qs = Entries.objects.all()
    totals = qs.aggregate(
        income=Sum(Case(When(ttype='IN', then='amount'), output_field=DecimalField())),
        expense=Sum(Case(When(ttype='EX', then='amount'), output_field=DecimalField())),
    )
    income = totals['income'] or 0
    expense = totals['expense'] or 0
    balance = income - expense
    return render(request, 'budget/dashboard.html', {'entries': qs[:50], 'income': income, 'expense': expense, 'balance': balance})

def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EntryForm()
    return render(request, 'budget/entry_form.html', {'form': form})

def entry_delete(request, pk):
    obj = get_object_or_404(Entries, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('dashboard')
    return render(request, 'budget/confirm_delete.html', {'object': obj})
