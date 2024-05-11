from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.name
    
class Editorial(models.Model):
    name = models.CharField(max_length=250)
    site = models.URLField()
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Books(models.Model):
    class Meta:
        verbose_name_plural = "Books"
    
    title = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=32)
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books')
    publishing_company = models.ForeignKey(Editorial, on_delete=models.PROTECT, related_name='books_company')
    authors =  models.ManyToManyField(Author, related_name='books_authors')
    
    def __str__(self):
        return "%s (%s) " %(self.title, self.publishing_company)
    
class Purchase(models.Model):
    class PurchaseStatus(models.IntegerChoices):
        CART = 1, 'Carrinho'
        REALIZED = 2, 'Realizado'
        PAID = 3, 'PAGO'
        DELIVERED = 4, 'Entregue'

    
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='my_shopping')
    status = models.IntegerField(choices=PurchaseStatus.choices, default=PurchaseStatus.CART)