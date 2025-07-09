from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Categories, Expenses, Incomes, Budgets


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_expense', 'created_by', 'created_at']
    list_filter = ['is_expense', 'created_at']
    search_fields = ['name', 'description']
    
    def get_queryset(self, request):
        # 全ユーザーが全カテゴリーを閲覧可能
        return super().get_queryset(request)
    
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        # 全ユーザーは自分が作成したデータのみ編集可能
        return obj.created_by == request.user
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        # 全ユーザーは自分が作成したデータのみ削除可能
        return obj.created_by == request.user


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'date', 'created_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['description', 'user__username', 'category__name']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # 管理者は全支出を閲覧可能
            return qs
        else:
            # 一般ユーザーは自分の支出のみ閲覧可能
            return qs.filter(user=request.user)
    
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        # 全ユーザーは自分が作成したデータのみ編集可能
        return obj.user == request.user
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        # 全ユーザーは自分が作成したデータのみ削除可能
        return obj.user == request.user


@admin.register(Incomes)
class IncomesAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'date', 'created_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['description', 'user__username', 'category__name']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # 管理者は全収入を閲覧可能
            return qs
        else:
            # 一般ユーザーは自分の収入のみ閲覧可能
            return qs.filter(user=request.user)
    
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        # 全ユーザーは自分が作成したデータのみ編集可能
        return obj.user == request.user
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        # 全ユーザーは自分が作成したデータのみ削除可能
        return obj.user == request.user


@admin.register(Budgets)
class BudgetsAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'period', 'start_date', 'end_date']
    list_filter = ['period', 'start_date', 'end_date']
    search_fields = ['description', 'user__username', 'category__name']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # 管理者は全予算を閲覧可能
            return qs
        else:
            # 一般ユーザーは自分の予算のみ閲覧可能
            return qs.filter(user=request.user)
    
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        # 全ユーザーは自分が作成したデータのみ編集可能
        return obj.user == request.user
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        # 全ユーザーは自分が作成したデータのみ削除可能
        return obj.user == request.user
