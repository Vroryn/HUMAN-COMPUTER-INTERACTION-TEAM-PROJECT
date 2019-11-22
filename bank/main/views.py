from django.shortcuts import render
# allows http requests
from django.http import HttpResponse
# Create your views here.

from .models import checkingAcct

def index(request):
    #HttpResponse takes html code as parameter
    return render(request,'main/login.html')

def main_page(request):
    return render(request,'main/home_page.html')

#added by Rene
def checking_acct_page(request):
    obj = checkingAcct.objects.get(transaction_id=1) 
    context = {

        'customer_id':obj.customer_id.customer_id.customer_id,
        'vendor' : obj.vendor_name
    }

    return render(request,'main/checking_acct_page.html', context)