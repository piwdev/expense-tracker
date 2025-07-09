from django.contrib import admin
from .models import Categories, Expenses, Incomes, Budgets

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_expense', 'created_by', 'created_at']
    list_filter = ['is_expense', 'created_at']
    search_fields = ['name', 'description']

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'date', 'created_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['description', 'user__username', 'category__name']

@admin.register(Incomes)
class IncomesAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'date', 'created_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['description', 'user__username', 'category__name']

@admin.register(Budgets)
class BudgetsAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'period', 'start_date', 'end_date']
    list_filter = ['period', 'start_date', 'end_date']
    search_fields = ['description', 'user__username', 'category__name']
