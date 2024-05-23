import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))
django.setup()

from app.models import Product, Promo, Detail


# Đọc dữ liệu từ tệp JSON
with open('product.json') as file:
    products = json.load(file)

# Nhập dữ liệu vào cơ sở dữ liệu
for product_data in products:
    promo_data = product_data.pop('promo')
    detail_data = product_data.pop('detail')
    
    promo = Promo.objects.create(**promo_data)
    detail = Detail.objects.create(**detail_data)
    Product.objects.create(promo=promo, details=detail, **product_data)

print('Products imported successfully')
