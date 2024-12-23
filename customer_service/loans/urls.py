from django.urls import path
from . import views

urlpatterns = [
    path('loans/', views.loans_list, name='loans-list'),
]
