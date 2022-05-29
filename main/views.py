from django.shortcuts import render, redirect
from .forms import UserDateForm


def index(request):
    if request.method == 'POST':
        form = UserDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            week = int(date.strftime("%U")) + 1
            return render(request, 'main/week.html', {'week': week, 'date': date})
    else:
        form = UserDateForm()
    return render(request, 'main/index.html', {'form': form})


def result(request, week, date):
    return render(request, 'main/week.html', {'week': week, 'date': date})
