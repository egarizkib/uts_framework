from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang, Jenis, Member

def produk(request):
    return render(request,'produk.html')
def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)
def Barang_View(request):
    barangs=Barang.objects.all()
    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def jenis(request):
    jeniss=Jenis.objects.all()
    konteks={
        'jeniss':jeniss,
    }
    return render(request,'jenis.html',konteks)

def member(request):
    members=Member.objects.all()
    
    konteks={
        'members':members,
    }
    return render(request,'member.html',konteks) 