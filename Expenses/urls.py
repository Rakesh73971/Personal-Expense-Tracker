from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories',views.CategoryViewset,basename='category'),
router.register('expenses',views.ExpenseViewSet,basename='expense')

urlpatterns = [
    path('',include(router.urls))
]