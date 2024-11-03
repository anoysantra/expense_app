from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),  # List all expenses
    path('create/', views.create_expense, name='create_expense'),  # Create a new expense
    path('update/<int:pk>/', views.update_expense, name='update_expense'),  # Update an existing expense
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),  # Delete an expense
    path('by_month/', views.expense_by_month, name='expense_by_month'),
    path('category/',views.expense_category, name='expense_by_category'),  # View expenses by month
]
