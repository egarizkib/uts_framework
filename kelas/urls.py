"""kelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk, tambah_barang, Barang_View, jenis, member

def LJ(request):
    return HttpResponse('Selamat datang LJ')

def LJ2(request):
    return render(request,'index.html')

def LJ2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'index.html',konteks)

def LJ3(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LJ2, name="index"),
    path('produk/' ,LJ3, name="produk"),
    path('addbrg/',tambah_barang),
    path('Vbrg/',Barang_View, name="Vbrg"),
    path('jenis/',jenis, name="jenis"),
    path('member/',member, name = "member")

]
