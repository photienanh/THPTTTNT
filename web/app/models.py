from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
class Promo(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
class Detail(models.Model):
    screen = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    camara = models.CharField(max_length=200)
    camaraFront = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    rom = models.CharField(max_length=200)
    microUSB = models.CharField(max_length=200)
    battery = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    star = models.IntegerField(default=0)
    rateCount = models.IntegerField(default=0)
    promo = models.OneToOneField(Promo, on_delete=models.CASCADE)
    detail = models.OneToOneField(Detail, on_delete=models.CASCADE)
class Payment(models.Model):
    ID = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_payment = models.DateField()
    method_payment = models.CharField(max_length=200)
class ShopCart(models.Model):
    ID = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class ShopOder(models.Model):
    ID = models.AutoField(primary_key=True)
    dateorder = models.DateField()
    totalprice = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    satatus_oder = models.CharField(max_length=200)
    shippingid = models.CharField(max_length=200)

class UserAccount(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    account_id = models.AutoField(primary_key=True)

class UserComment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    post_id = models.AutoField(primary_key=True)
    
    