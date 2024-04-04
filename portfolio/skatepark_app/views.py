from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .forms import SkateparkForm
from .models import Skatepark
# Create your views here. 
def index(request): 
    # Render the HTML template index.html with the data in the context variable. 
    return render( request, 'skatepark_app/index.html', {'skatepark_objects' : Skatepark.objects.all()})

# listings/views.py


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
