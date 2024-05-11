from django.contrib import admin
from .models import Category, Editorial, Author, Books, Purchase


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','site')
    
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'ISBN', 'quantity', 'price', 'category', 'publishing_company', )

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')