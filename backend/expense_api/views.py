from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import date
from .models import Categories, Expenses, Incomes, Budgets
from .serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer, BudgetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Category's ViewSet"""
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'created_at']
    ordering = ['name']
    
    def get_queryset(self):
        return Categories.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ExpenseViewSet(viewsets.ModelViewSet):
    """Expense's ViewSet"""
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'amount', 'created_at']
    ordering = ['-date', '-created_at']
    
    def get_queryset(self):
        queryset = Expenses.objects.filter(user=self.request.user)
        
        # filter
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


class IncomeViewSet(viewsets.ModelViewSet):
    """Income's ViewSet"""
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'amount', 'created_at']
    ordering = ['-date', '-created_at']
    
    def get_queryset(self):
        queryset = Incomes.objects.filter(user=self.request.user)
        
        # filter
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


class BudgetViewSet(viewsets.ModelViewSet):
    """Budget's ViewSet"""
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_date', 'amount', 'created_at']
    ordering = ['-start_date', '-created_at']
    
    def get_queryset(self):
        return Budgets.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def monthly_summary(request):
    """月別支出サマリー"""
    # パラメータ処理
    year = int(request.GET.get('year', timezone.now().year))
    month = int(request.GET.get('month', timezone.now().month))
    
    # 該当月の支出を取得
    expenses = Expenses.objects.filter(
        user=request.user,
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