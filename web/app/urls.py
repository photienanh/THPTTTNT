from django.urls import path
from django.contrib import admin
from . import views
from .views import product

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

    path('product/',product, name='product'),
]
