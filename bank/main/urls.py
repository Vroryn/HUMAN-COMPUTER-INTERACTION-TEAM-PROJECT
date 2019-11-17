#urls.py for main
from django.urls import path
#import views from current directory
from . import views

urlpatterns = [
path("",views.index, name = "index"), #http response for home page
path("main_page/",views.main_page,name = "main page"),
]
