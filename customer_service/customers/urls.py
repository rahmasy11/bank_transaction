from django.urls import path
from .views import CustomerViewSet

urlpatterns = [
    path('customers/', CustomerViewSet.as_view({'get': 'list'}), name='customer-list'),
]
