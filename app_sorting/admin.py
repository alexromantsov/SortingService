from django.contrib import admin
from .models import SortingFunction


class SortingFunctionAdmin(admin.ModelAdmin):
    list_display = ('module_name', 'function_name', 'description')
    search_fields = ('module_name', 'function_name',)
    list_filter = ('module_name',)


admin.site.register(SortingFunction, SortingFunctionAdmin)
