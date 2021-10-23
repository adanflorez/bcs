from django.contrib import admin

from budget.models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date', 'created_at', 'amount', 'category']
