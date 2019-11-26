from django.shortcuts import render
# allows http requests
from django.http import HttpResponse
# Create your views here.

from .models import checkingAcct
from .models import Accounts

from django.db.models import Sum


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
def checking_acct_page(request, customer_number, account_number):
    #obj = checkingAcct.objects.all()
    customerID = checkingAcct.objects.first()
    account_number = customerID.account_number.account_number
    account_balance = Accounts.objects.first().account_balance

     #pull account info for the given customer number and account number
    checking_info = checkingAcct.objects.filter(customer_id=customer_number, account_number = account_number) #checkingAcct.objects.all()

     
    balance = checkingAcct.objects.aggregate(balance_sum = Sum('amount'))['balance_sum'] #sums all the amounts and returns the value from the dictionary returned
    
    
     
    if request.user.is_authenticated:
        account_balance = balance
        current_user = request.user
    else:
        account_balance = 300
        current_user = request.user


    context = {
       'checking_posts': checking_info, #checkingAcct.objects.all(),
        'customerID': customer_number,#customerID.customer_id.customer_id.customer_id,
        'account_number': account_number,
        'account_balance': account_balance,
        'current_user': current_user
    }

   # return render(request,'main/checking_acct_page.html', context)
    if request.user.is_authenticated:
           return render(request,'main/checking_acct_page.html', context)
    else:
           return render(request,'main/login.html', context)

       
