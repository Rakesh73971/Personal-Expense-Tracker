from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.Expense)
class AdminExpense(admin.ModelAdmin):
    list_display = ['category','title','amount','payment_method']
    autocomplete_fields = ['category']


