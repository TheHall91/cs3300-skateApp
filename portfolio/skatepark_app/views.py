from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .forms import SkateparkForm, CreateUserForm
from .models import Skatepark
from django.db.models import Q
from django.conf import settings
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here. 

def index(request): 
    # Render the HTML template index.html with the data in the context variable. 
    return render( request, 'skatepark_app/index.html', {'skatepark_objects' : Skatepark.objects.all()})

# listings/views.py


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('allParks')
            else:
                messages.info(request, 'Username/Password is incorrect')
        return render(request, 'registration/login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Created For ' + user)
                return redirect('login')
        return render(request, 'registration/register.html', {'form' : form })


class SearchResultsView(ListView):
    model = Skatepark
    template_name = 'skatepark_app/search.html'
    queryset = Skatepark.objects.filter(name__icontains='Goose')
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Skatepark.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query) | Q(difficulty__icontains=query)
        )
        return object_list


def skatepark_detail(request, id):
  skate = Skatepark.objects.get(id=id)
  test_display=Skatepark.objects.prefetch_related('reviews').get(id=id)
  key = settings.GOOGLE_MAPS_API_KEY
  return render(request, 'skatepark_app/skatepark_detail.html', {'skate' : skate, 'key': key}) 
...

@login_required(login_url='login')
def skatepark_create(request):

    if request.method == 'POST':
        form = SkateparkForm(request.POST)
        if form.is_valid():
            park = form.save()
            return redirect('index')

    else:
        form = SkateparkForm()
    return render(request,
            'skatepark_app/create_skatepark.html',
            {'form': form})

@login_required(login_url='login')
def skatepark_update(request, id):
    skate = Skatepark.objects.get(id=id)

    if request.method == 'POST':
        form = SkateparkForm(request.POST, instance=skate)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('skatepark-detail', skate.id)
    else:
        form = SkateparkForm(instance=skate)

    return render(request,'skatepark_app/skatepark_update.html', {'form': form})

@login_required(login_url='login')
def skatepark_delete(request, id):
    skate = Skatepark.objects.get(id=id)
    # listings/views.py
    if request.method == 'POST':
        # delete the band from the database
        skate.delete()
        # redirect to the bands list
        return redirect('index')
    # no need for an `else` here. If it's a GET request, just continue
    return render(request,'skatepark_app/skatepark_delete.html',{'skate' : skate})


def skatepark_listall(request): 
    # Render the HTML template index.html with the data in the context variable. 
    return render( request, 'skatepark_app/skatepark_listall.html', {'skatepark_objects' : Skatepark.objects.all()})


