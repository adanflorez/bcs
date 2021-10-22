from django.contrib import admin

from revenue.models import Revenue


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ['subject', 'amount', 'created_at', 'budget_date', 'slug']
