from rest_framework import serializers
from .models import Categories, Expenses, Incomes, Budgets


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'description', 'is_expense', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']


class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Expenses
        fields = ['id', 'user', 'category', 'category_name', 'amount', 'description', 'date', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']


class IncomeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Incomes
        fields = ['id', 'user', 'category', 'category_name', 'amount', 'description', 'date', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']


class BudgetSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Budgets
        fields = ['id', 'user', 'category', 'category_name', 'description', 'amount', 'period', 'start_date', 'end_date', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at'] 