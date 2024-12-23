#from django.contrib import admin
#from .models import Loan

#@admin.register(Loan)
#class LoanAdmin(admin.ModelAdmin):
    #list_display = ('customer', 'loan_type', 'loan_amount', 'status')


from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'loan_type', 'amount', 'interest_rate', 'duration_months', 'created_at')
