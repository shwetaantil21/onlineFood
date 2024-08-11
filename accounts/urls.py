from django.urls import path
from .import views
# Create urls here

urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
     path('registerVendor/', views.registerVendor, name='registerVendor'),
]
