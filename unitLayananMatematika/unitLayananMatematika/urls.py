"""unitLayananMatematika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from layanan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profil/', views.profil),
    path('visi/', views.visi),
    path('struktur/', views.struktur),
    path('dosen/', views.dosen),
    path('akreditasi/', views.akreditasi),
    path('pedoman/', views.pedoman),
    path('kalender/', views.kalender),
    path('fasilitas/', views.fasilitas),
    path('kurikulum/', views.kurikulum),
    path('beasiswa/', views.beasiswa),
    path('kegiatan/', views.kegiatan),
    path('mahasiswa/', views.mahasiswa),
    path('prestasi/', views.prestasi),
    path('statistik/', views.statistik),
    path('tahapan/', views.tahapan),
    path('tracer/', views.tracer),
    path('penelitian/', views.penelitian),
    path('pengabdian/', views.pengabdian),
    path('spada/', views.spada),
    path('siakad/', views.siakad),
    path('silatta/', views.silatta),
]