from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .forms import SkateparkForm, CreateUserForm
from .models import Skatepark
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here. 

def index(request): 
    # Render the HTML template index.html with the data in the context variable. 
    return render( request, 'skatepark_app/index.html', {'skatepark_objects' : Skatepark.objects.all()})

# listings/views.py


def loginPage(request):
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


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Created For ' + user)
            return redirect('login')
    return render(request, 'registration/register.html', {'form' : form })


def skatepark_detail(request, id):
  skate = Skatepark.objects.get(id=id) # we insert this line to get the Band with that id
  return render(request, 'skatepark_app/skatepark_detail.html',{'skate': skate}) # we update this line to pass the band to the template
...
def skatepark_create(request):
   # listings/views.py

    if request.method == 'POST':
        form = SkateparkForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            park = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('index')

    else:
        form = SkateparkForm()
    return render(request,
            'skatepark_app/create_skatepark.html',
            {'form': form})

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


