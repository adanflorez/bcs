from django.contrib import admin

from budget.models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'period', 'created_at', 'amount', 'remaining']
