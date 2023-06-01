from django.db import models

class Author(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name

        
class Book(models.Model):
    name = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    publisher= models.ForeignKey(Publisher, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/images/')
    Author= models.ManyToManyField(Author)
    def __str__(self):
        return self.name