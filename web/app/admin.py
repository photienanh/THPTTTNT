from django.contrib import admin

# Register your models here.
from .models import User,Promo,Detail,Product,Payment,Shipping,ShopCart,ShopOrder,UserAccount,UserComment
admin.site.register(User)
admin.site.register(Promo)
admin.site.register(Detail)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Shipping)
admin.site.register(ShopCart)
admin.site.register(ShopOrder)
admin.site.register(UserAccount)
admin.site.register(UserComment)