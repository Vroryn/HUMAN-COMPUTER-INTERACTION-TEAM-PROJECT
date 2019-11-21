from django.shortcuts import render
# allows http requests
from django.http import HttpResponse
# Create your views here.

def index(request):
    #HttpResponse takes html code as parameter
    return render(request,'main/login.html')

def main_page(request):
    return render(request,'main/home_page.html')

#added by Rene
def checking_acct_page(request):
    return render(request,'main/checking_acct_page.html')