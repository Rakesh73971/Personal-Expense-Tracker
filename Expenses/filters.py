from django_filters.rest_framework import FilterSet
from .models import Expense

class ExpenseFilter(FilterSet):
    class Meta:
        model = Expense
        fields = {
            'category':['exact'],
            'payment_method':['exact'],
            'date':['lt','gt']
        }