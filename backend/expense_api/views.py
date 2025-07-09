from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import datetime, date
from .models import Categories, Expenses, Incomes, Budgets
from .serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer, BudgetSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryViewSet(viewsets.ModelViewSet):
    """カテゴリーのViewSet"""
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'created_at']
    ordering = ['name']
    
    def get_queryset(self):
        # 全ユーザーが全カテゴリーを閲覧可能
        queryset = Categories.objects.all()
        
        # カテゴリータイプでフィルタリング
        is_expense = self.request.query_params.get('is_expense')
        if is_expense is not None:
            is_expense_bool = is_expense.lower() == 'true'
            queryset = queryset.filter(is_expense=is_expense_bool)
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def perform_update(self, serializer):
        # 全ユーザーは自分が作成したデータのみ編集可能
        instance = serializer.instance
        if instance.created_by != self.request.user:
            raise PermissionError("自分が作成したデータのみ編集可能です")
        serializer.save()


class ExpenseViewSet(viewsets.ModelViewSet):
    """支出のViewSet"""
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'amount', 'created_at']
    ordering = ['-date', '-created_at']
    
    def get_queryset(self):
        user = self.request.user
        
        # 管理者は全支出を閲覧可能、一般ユーザーは自分の支出のみ閲覧可能
        if user.is_superuser:
            queryset = Expenses.objects.all()
        else:
            queryset = Expenses.objects.filter(user=user)
        
        # フィルタリング機能
        category = self.request.query_params.get('category')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        search = self.request.query_params.get('search')
        
        if category:
            queryset = queryset.filter(category_id=category)
        
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        
        if search:
            queryset = queryset.filter(
                Q(description__icontains=search) | 
                Q(category__name__icontains=search)
            )
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        # 全ユーザーは自分が作成したデータのみ編集可能
        instance = serializer.instance
        if instance.user != self.request.user:
            raise PermissionError("自分が作成したデータのみ編集可能です")
        serializer.save()


class IncomeViewSet(viewsets.ModelViewSet):
    """収入のViewSet"""
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'amount', 'created_at']
    ordering = ['-date', '-created_at']
    
    def get_queryset(self):
        user = self.request.user
        
        # 管理者は全収入を閲覧可能、一般ユーザーは自分の収入のみ閲覧可能
        if user.is_superuser:
            queryset = Incomes.objects.all()
        else:
            queryset = Incomes.objects.filter(user=user)
        
        # フィルタリング機能
        category = self.request.query_params.get('category')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        search = self.request.query_params.get('search')
        
        if category:
            queryset = queryset.filter(category_id=category)
        
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        
        if search:
            queryset = queryset.filter(
                Q(description__icontains=search) | 
                Q(category__name__icontains=search)
            )
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        # 全ユーザーは自分が作成したデータのみ編集可能
        instance = serializer.instance
        if instance.user != self.request.user:
            raise PermissionError("自分が作成したデータのみ編集可能です")
        serializer.save()


class BudgetViewSet(viewsets.ModelViewSet):
    """予算のViewSet"""
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_date', 'amount', 'created_at']
    ordering = ['-start_date', '-created_at']
    
    def get_queryset(self):
        user = self.request.user
        
        # 管理者は全予算を閲覧可能、一般ユーザーは自分の予算のみ閲覧可能
        if user.is_superuser:
            queryset = Budgets.objects.all()
        else:
            queryset = Budgets.objects.filter(user=user)
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        # 全ユーザーは自分が作成したデータのみ編集可能
        instance = serializer.instance
        if instance.user != self.request.user:
            raise PermissionError("自分が作成したデータのみ編集可能です")
        serializer.save()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def monthly_summary(request):
    """月別支出サマリー"""
    user = request.user
    
    # パラメータ処理
    year = int(request.GET.get('year', timezone.now().year))
    month = int(request.GET.get('month', timezone.now().month))
    
    # 管理者は全ユーザーの支出を集計、一般ユーザーは自分の支出のみ
    if user.is_superuser:
        expenses = Expenses.objects.filter(
            date__year=year,
            date__month=month
        )
    else:
        expenses = Expenses.objects.filter(
            user=user,
            date__year=year,
            date__month=month
        )
    
    # 総支出額
    total = expenses.aggregate(total=Sum('amount'))['total'] or 0
    
    # カテゴリ別集計
    by_category = expenses.values(
        'category__name'
    ).annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-total')
    
    # パーセンテージ計算
    for item in by_category:
        if total > 0:
            item['percentage'] = round((item['total'] / total) * 100, 1)
        else:
            item['percentage'] = 0
    
    # 日別集計
    daily_totals = expenses.values('date').annotate(
        total=Sum('amount')
    ).order_by('-date')[:7]  # 最近7日間
    
    return Response({
        'period': {
            'year': year,
            'month': month,
            'month_name': date(year, month, 1).strftime('%B')
        },
        'total': total,
        'by_category': list(by_category),
        'daily_totals': list(daily_totals)
    })