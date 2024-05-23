from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=200)

class Promo(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

class Detail(models.Model):
    screen = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    camera = models.CharField(max_length=200)
    camera_front = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    rom = models.CharField(max_length=200)
    micro_usb = models.CharField(max_length=200)
    sim = models.CharField(max_length=200)
    battery = models.CharField(max_length=200)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    img = models.ImageField()
    price = models.CharField(max_length=255)
    star = models.IntegerField(default=0)
    rateCount = models.IntegerField(default=0)
    promo = models.OneToOneField(Promo, on_delete=models.CASCADE)
    details = models.OneToOneField(Detail, on_delete=models.CASCADE)

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_payment = models.DateField()
    method_payment = models.CharField(max_length=200)

class Shipping(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    kind = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    price = models.FloatField()


class ShopCart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class ShopOrder(models.Model):
    id = models.AutoField(primary_key=True)
    date_order = models.DateField()
    total_price = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    status_order = models.CharField(max_length=200)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)

class UserAccount(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)

class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
