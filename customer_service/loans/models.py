#from django.db import models
#from customers.models import Customer

#class Loan(models.Model):
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #loan_type = models.CharField(max_length=50)  # e.g., Home, Personal, Education
    #loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    #status = models.CharField(max_length=20, choices=[
        #('Pending', 'Pending'),
        #('Approved', 'Approved'),
        #('Rejected', 'Rejected'),
    #])
    #created_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
        #return f"Loan {self.loan_type} for {self.customer.first_name}"

from django.db import models
from customers.models import Customer

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    loan_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    duration_months = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan for {self.customer} - {self.amount} @ {self.interest_rate}%"


