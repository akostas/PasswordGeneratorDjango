from django.urls import path
from .views import password_view

urlpatterns = [
    path('generate/', password_view, name='generate_password'),
]
