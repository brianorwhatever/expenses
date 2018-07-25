from django.contrib import admin
from django.urls import path

from .views import create_expense, edit_expense

urlpatterns = [
    path('', create_expense),
    path('<expense_id>', edit_expense)
]