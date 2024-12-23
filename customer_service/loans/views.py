from django.shortcuts import render
from .models import Loan

def loans_list(request):
    loans = Loan.objects.all()
    return render(request, 'loans/loans_list.html', {'loans': loans})
