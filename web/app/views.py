from django.shortcuts import render
from .models import Product, Promo, Detail
from django.http import JsonResponse

def index(request):
    return render(request, 'app/index.html')
def admin(request):
    return render(request, 'app/admin.html')
def chitietsanpham(request):
    return render(request, 'app/chitietsanpham.html')
def createProductJson(request):
    return render(request, 'app/createProductJson.html')
def giohang(request):
    return render(request, 'app/giohang.html')
def gioithieu(request):
    return render(request, 'app/gioithieu.html')
def lienhe(request):
    return render(request, 'app/lienhe.html')
def nguoidung(request):
    return render(request, 'app/nguoidung.html')
def tintuc(request):
    return render(request, 'app/tintuc.html')
def trungtambaohanh(request):
    return render(request, 'app/trungtambaohanh.html')
def tuyendung(request):
    return render(request, 'app/tuyendung.html')


def product(request):
    products = Product.objects.all().values()  # Lấy tất cả sản phẩm từ cơ sở dữ liệu
    promos = Promo.objects.all().values()  # Lấy tất cả thông tin khuyến mãi
    details = Detail.objects.all().values()  # Lấy tất cả thông tin chi tiết sản phẩm
    return JsonResponse(request,{'products': products, 'promos': promos, 'details': details})

