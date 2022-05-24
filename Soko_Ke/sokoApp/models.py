from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=400)
    email = models.EmailField(max_length=150,unique=True)
    password = models.CharField(max_length=150)
    address = models.TextField(max_length=600)
    phone = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)

class Store(models.Model):
    userId = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    creat_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    title = models.ForeignKey(User)
    storeId = models.ForeignKey(Store)
    category = models.CharField(max_length=150)
    price = models.IntegerField()
    stock = models.IntegerField()
    condition = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)


class ProductImg(models.Model):
    productId = models.ForeignKey(Product)
    url = models.CharField(max_length=300)


class Cart(models.Model):
    productId = models.ForeignKey(Product)
    quantity = models.IntegerField()
    

class CartItem(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE())
    productId = models.ForeignKey(Product, on_delete=models.CASCADE())
    quantity = models.IntegerField()

def upload_location(instance, filename):
    ext = filename.split(".")[-1]
    return "%s/%s"("img",datetime.now(),ext)

class FileUpload(models.Model):
    cartId = models.ForeignKey(Cart)
