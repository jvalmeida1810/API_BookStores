from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from author.models import Author
from editorial.models import Editorial

class Category(models.Model):
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
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books_category')
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
    
    #atributo imaginário no banco de dados
    @property 
    def total(self): 
        #multiplicando quantidade e preço de livros com F
        queryset = self.items.all().aggregate(
            total=models.Sum(F('quantity') * F('books__price'))
        )
        return queryset['total']

class PurchaseItems(models.Model):
    class Meta:
  
        verbose_name_plural = "Purchase Items"
            
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
    books = models.ForeignKey(Books, on_delete=models.PROTECT, related_name='+')
    quantity = models.IntegerField()
    
    
    
    