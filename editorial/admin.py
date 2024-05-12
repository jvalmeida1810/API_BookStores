from django.contrib import admin
from .models import Editorial

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','site')
    