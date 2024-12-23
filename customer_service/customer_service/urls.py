
#from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from customers.views import CustomerViewSet

#router = DefaultRouter()
#router.register(r'customers', CustomerViewSet)

#urlpatterns = [
    #path('api/', include(router.urls)),
#]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('customers.urls')),
    path('api/', include('loans.urls')),  # Add this line for loans
]



