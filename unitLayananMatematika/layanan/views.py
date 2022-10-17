from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profil(request):
    return render(request, 'profil.html')

def visi(request):
    return render(request, 'visi.html')

def struktur(request):
    return render(request, 'struktur.html')

def dosen(request):
    return render(request, 'dosen.html')

def akreditasi(request):
    return render(request, 'akreditasi.html')

def pedoman(request):
    return render(request, 'pedoman.html')

def kalender(request):
    return render(request, 'kalender.html')

def fasilitas(request):
    return render(request, 'fasilitas.html')

def kurikulum(request):
    return render(request, 'kurikulum.html')

def beasiswa(request):
    return render(request, 'beasiswa.html')

def kegiatan(request):
    return render(request, 'kegiatan.html')

def mahasiswa(request):
    return render(request, 'mahasiswa.html')

def prestasi(request):
    return render(request, 'prestasi.html')

def statistik(request):
    return render(request, 'statistik.html')
    
def tahapan(request):
    return render(request, 'tahapan.html')

def tracer(request):
    return render(request, 'tracer.html')

def penelitian(request):
    return render(request, 'penelitian.html')

def pengabdian(request):
    return render(request, 'pengabdian.html')

def spada(request):
    return render(request, 'spada.html')

def siakad(request):
    return render(request, 'siakad.html')

def silatta(request):
    return render(request, 'silatta.html')

