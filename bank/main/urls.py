#urls.py for main
from django.urls import path
#import views from current directory
from . import views
from main.views import checking_acct_page

#added by Kevin
urlpatterns = [
path("",views.index, name = "index"), #http response for home page
path("main_page/",views.main_page,name = "main page"),
path("promotion_1/",views.promotion_1,name ="promotion 1"),
path("promotion_2/",views.promotion_2,name ="promotion 2"),
path("promotion_3/",views.promotion_3,name ="promotion 3"),
path("promotion_4/",views.promotion_4,name ="promotion 4"),
path("promotion_5/",views.promotion_5,name ="promotion 5"),
path("promotion_6/",views.promotion_6,name ="promotion 6"),
path("manage_account/",views.manage_account,name = "manage account"),
path("account_summary/",views.account_summary,name="account summary"),
#path("checking_acct_page/", checking_acct_page, name = "checking_acct_page") #added by rene
path("main_page/<int:customer_number>/<int:account_number>/checking_acct_page/", views.checking_acct_page, name = "checking_acct_page") #added by rene
]
