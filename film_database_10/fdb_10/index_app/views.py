
from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm


# Create your views here.

def index(request):
    film = Film.objects.all()
    return render(request, 'index.html', {'film_list': film})


def detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, 'detail.html', {'film_list': film})

def redirect_f(request):
    return redirect('/')


def add_film(request):
    if request.method == "POST":
        f_name = request.POST.get('name',)
        f_year = request.POST.get('year',)
        f_genre = request.POST.get('genre',)
        f_prate = request.POST.get('prate',)
        f_cast = request.POST.get('cast',)
        f_dir = request.POST.get('dir',)
        f_plot = request.POST.get('plot',)
        f_img = request.FILES['img']
        film = Film(f_name=f_name, f_year=f_year, f_genre=f_genre, f_prate=f_prate, f_cast=f_cast, f_dir=f_dir, f_plot=f_plot, f_img=f_img)
        film.save()
        return redirect('/')
    return render(request, 'add_film.html')


def update_film(request,id):
    film = Film.objects.get(id=id)
    form = FilmForm(request.POST or None, request.FILES, instance=film)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'film': film})

def delete_film(request,id):
    if request.method == "POST":
        film = Film.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request, 'delete.html')

