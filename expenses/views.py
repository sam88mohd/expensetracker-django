from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request=request, template_name='expenses/index.html')


def add_expense(request):
    return render(request=request, template_name='expenses/add_expense.html')
