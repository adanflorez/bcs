from django.contrib import admin

from expense.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'description', 'amount', 'created_at']
