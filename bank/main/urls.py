#urls.py for main
from django.urls import path
#import views from current directory
from . import views
from main.views import checking_acct_page


urlpatterns = [
path("",views.index, name = "index"), #http response for home page
path("main_page/",views.main_page,name = "main page"),
path("checking_acct_page/", checking_acct_page, name = "checking_acct_page") #added by rene
]
