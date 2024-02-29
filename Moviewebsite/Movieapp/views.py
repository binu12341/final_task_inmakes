from django.contrib import auth, messages
from django.db.models import Q
from .forms import EditProfileForm, MovieForm
from .models import User_registration, Add_movies
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def index(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            request.session['username'] = user.id
            return redirect('home')
        else:

            context = {'msg_error': 'Invalid data'}
        return render(request, 'home.html', context)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User_registration.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect('register')
        elif User_registration.objects.filter(email=email).exists():
            messages.info(request, "email already taken")
            return redirect('register')
        elif User_registration.objects.filter(password=password).exists():
            messages.info(request, "password already taken")
            return redirect('register')
        else:
            user = User_registration(username=username, firstname=firstname, lastname=lastname, email=email,password=password)
            user.save()

        return render(request,'success.html')
    return render(request,'register.html')

def user_profile(request):
    user=User_registration.objects.all()
    return render(request,'user_profile.html',{'user':user})

def edit(request,id):
    pro = User_registration.objects.get(id=id)
    form = EditProfileForm(request.POST or None, instance=pro)
    if form.is_valid():
        form.save()
        return redirect('user_profile')
    return render(request, 'update.html', {'form': form, 'pro': pro})

def back(request):
    bk=Add_movies.objects.all()
    return render(request, 'home.html',{'bk':bk})


def add_movie(request):
    if request.method=="POST":
        film = Add_movies()
        film.movie_title=request.POST['movie_title']
        film.slug = request.POST['slug']
        film.poster = request.FILES['poster']
        film.description = request.POST['description']
        film.release_date = request.POST['release_date']
        film.actors = request.POST['actors']
        film.category = request.POST['category']
        film.YouTube_trailer_link = request.POST['YouTube_trailer_link']
        movie=Add_movies(movie_title=film.movie_title,slug=film.slug,poster=film.poster,description=film.description,release_date=film.release_date,actors=film.actors,category=film.category,YouTube_trailer_link=film.YouTube_trailer_link)
        movie.save()
        return redirect('allMov')
    return render(request,'addmovie.html')

def allMov(request):
    movies_list = Add_movies.objects.all()
    return render(request,'category.html',{'movies_list':movies_list})


def MovDetail(request,c_slug=None):
    c_page = None
    movies_list = None
    if c_slug != None:
        c_page = get_object_or_404(Add_movies, slug=c_slug)
        movies_list = Add_movies.objects.all().filter(category=c_page)
    return render(request, 'movdetail.html', {'category': c_page, 'movies_list': movies_list})

def update(request,id):
    movie=Add_movies.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('allMov')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    movie = Add_movies.objects.get(id=id)
    movie.delete()
    return redirect('index')


def cancel(request,id):
    bk=Add_movies.objects.get(id=id)
    return render(request, 'category.html',{'bk':bk})

def SearchResult(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies=Add_movies.objects.all().filter(Q(movie_title__contains=query) | Q(category__contains=query))
        return render(request,'search.html',{'query':query,'movies':movies})


def logout(request):
    auth.logout(request)
    return redirect('login')