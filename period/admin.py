from django.contrib import admin

from period.models import Period


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date']
