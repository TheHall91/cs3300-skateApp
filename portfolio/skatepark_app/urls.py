from django.urls import path 
from . import views 
from django.conf.urls import include
urlpatterns = [ 
    #path function defines a url pattern #'' is empty to represent 
    # based path to app # views.index is the function defined in views.py 
    # name='index' parameter is to dynamically create url 
    # # example in html <a href="{% url 'index' %}">Home</a>. 
    path('', views.index, name='index'),
    path('allParks', views.skatepark_listall, name='skatepark-listall'),
    path('addSkatePark', views.skatepark_create, name='skatepark-create'),
    path('<int:id>', views.skatepark_detail, name='skatepark-detail'),
    path('<int:id>/update', views.skatepark_update, name='skatepark-update'),
    path('<int:id>/delete', views.skatepark_delete, name='skatepark-delete'),
    path('accounts/register', views.registerPage, name='register'),
    path('accounts/login', views.loginPage, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('register', ),
    #accounts/ login/ [name='login']
    #accounts/ logout/ [name='logout']
    ]