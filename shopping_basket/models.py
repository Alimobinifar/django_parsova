from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class FinalShoppingBasket(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateTimeField()


class ShoppingBasket(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateTimeField()
    ShoppingBasket = models.ForeignKey(FinalShoppingBasket, on_delete=models.CASCADE)
    basket_status= [('ok', 'payment success'),('pending','waiting for . '),('cancell', 'cancelled')]
    status = models.CharField(max_length=20,choices=basket_status,default='pending')