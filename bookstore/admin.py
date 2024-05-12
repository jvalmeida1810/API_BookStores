from django.contrib import admin
from .models import Category, Books, Purchase, PurchaseItems

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'ISBN', 'quantity', 'price', 'category', 'publishing_company', )
    
class ItemsInline(admin.StackedInline):
    model = PurchaseItems

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    inlines = (ItemsInline,)    