from django.db import models

class Color(models.Model):
    color = models.CharField(max_length= 20)
    
    def __str__(self):
        return str(self.color)
        
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.ManyToManyField(Color)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=1000)
    image1 = models.CharField(max_length=1000)
    image2 = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100, default="Sobre medidas")
    offert = models.BooleanField(default=False)
    stock = models.IntegerField(default=1, null=False, blank=False)
    
    
    def __str__(self):
        return str(self.name)