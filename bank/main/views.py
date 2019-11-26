from django.shortcuts import render
# allows http requests
from django.http import HttpResponse
# Create your views here.

from .models import checkingAcct


######## added by Kevin ############
def index(request):
    #HttpResponse takes html code as parameter
    return render(request,'main/login.html')

def main_page(request):
    return render(request,'main/home_page.html')

def account_summary(request):
    return render(request,'main/account_summary.html')

def promotion_1(request):
    return render(request,'main/promotion1.html')

def promotion_2(request):
    return render(request,'main/promotion2.html')

def promotion_3(request):
    return render(request,'main/promotion3.html')

def promotion_4(request):
    return render(request,'main/promotion4.html')

def promotion_5(request):
    return render(request,'main/promotion5.html')

def promotion_6(request):
    return render(request,'main/promotion6.html')

def manage_account(request):
    return render(request,'main/manage_account.html')

######added by Kevin ##########

#added by Rene
def checking_acct_page(request):
    obj = checkingAcct.objects.get(transaction_id=1)
    context = {

        'customer_id':obj.customer_id.customer_id.customer_id,
        'vendor' : obj.vendor_name
    }

    return render(request,'main/checking_acct_page.html', context)
