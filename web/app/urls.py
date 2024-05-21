from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.admin),
    path('', views.chitietsanpham),
    path('', views.createProductJson),
    path('', views.giohang),
    path('', views.gioithieu),
    path('', views.lienhe),
    path('', views.nguoidung),
    path('', views.tintuc),
    path('', views.trungtambaohanh),
    path('', views.tuyendung),
]
