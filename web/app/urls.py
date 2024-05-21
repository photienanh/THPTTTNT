from django.urls import path
from django.contrib import admin
from . import views
import execjs

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('admin.html', views.admin),
    path('chitietsanpham.html', views.chitietsanpham),
    path('createProductJson.html', views.createProductJson),
    path('giohang.html', views.giohang),
    path('gioithieu.html', views.gioithieu),
    path('lienhe.html', views.lienhe),
    path('nguoidung.html', views.nguoidung),
    path('tintuc.html', views.tintuc),
    path('trungtambaohanh.html', views.trungtambaohanh),
    path('tuyendung.html', views.tuyendung),
]
with open('app/static/app/data/products.js', 'r') as file:
    js_code = file.read()
context = execjs.compile(js_code)
products = context.call("getProducts")
products.pop()
for product in products:
    name = product['name']
    name = name.replace(' ', '-')
    urlpatterns.append(path(f'chitietsanpham.html?{name}', views.chitietsanpham))