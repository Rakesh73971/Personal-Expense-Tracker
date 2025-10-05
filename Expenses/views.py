
from .models import Category,Expense
from .serializers import CategorySerializer,ExpenseSerializer,ExpenseListSerializer
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import ExpenseFilter



# Create your views here.

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ExpenseFilter
  

    def get_serializer_class(self):
        if self.action == 'list_with_total':
            return ExpenseListSerializer
        return ExpenseSerializer

    @action(detail=False, methods=['get'], url_path='with-total')
    def list_with_total(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ExpenseSerializer(page, many=True)
            total_amount = queryset.aggregate(total=Sum('amount'))['total'] or 0
            return self.get_paginated_response({
                'Expenses': serializer.data,
                'total_amount': float(total_amount)
            })
        
        serializer = ExpenseSerializer(queryset, many=True)
        total_amount = queryset.aggregate(total=Sum('amount'))['total'] or 0
        return Response({
            'Expenses': serializer.data,
            'total_amount': float(total_amount)
        })