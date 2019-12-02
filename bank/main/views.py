from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# allows http requests
from django.http import HttpResponse
# Create your views here.

from .models import checkingAcct
from .models import credit_cardAcct
from .models import Accounts
from .models import Users_bank
from .models import Customers_List
from .models import savingsAcct

from django.db.models import Sum

from .forms import UserRegisterForm #custom class for forms, added by Rene
from .forms import Profile_Edit_Form



######## added by Kevin ############
def index(request):
    #HttpResponse takes html code as parameter
    return render(request,'main/login.html')

####### addedy by Rene #######

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form =  UserRegisterForm()
    return render(request,'main/register.html', {'form': form})

####### end #############
def main_page(request):
    if request.user.is_authenticated:
         
         
        customer_found = Users_bank.objects.filter(username = request.user) #find the customer in the Users_bank table
       
        customer_found_id = customer_found.first().customer_id    #extract the customer id from the found user object.

        customer_info = Customers_List.objects.filter(customer_id = customer_found_id).first() #checkingAcct.objects.first()

        account_number_checking = Accounts.objects.filter(customer_id = customer_found_id, account_type = 'checking').first().account_number
        account_number_credit = Accounts.objects.filter(customer_id = customer_found_id, account_type = 'credit_card').first().account_number
        account_number_savings = Accounts.objects.filter(customer_id = customer_found_id, account_type = 'savings').first().account_number

        checking_info = checkingAcct.objects.filter(customer_id=customer_found_id, account_number = account_number_checking)
        checking_balance = checkingAcct.objects.filter(customer_id = customer_found_id).aggregate(balance_sum = Sum('amount'))['balance_sum'] 

        credit_info = credit_cardAcct.objects.filter(customer_id=customer_found_id, account_number = account_number_credit)
        credit_card_balance = credit_cardAcct.objects.filter(customer_id = customer_found_id).aggregate(balance_sum = Sum('amount'))['balance_sum']

        savings_info = savingsAcct.objects.filter(customer_id=customer_found_id, account_number = account_number_savings)
        savings_balance = savingsAcct.objects.filter(customer_id = customer_found_id).aggregate(balance_sum = Sum('amount'))['balance_sum']


        request.session['customer_id_num'] = str(customer_found_id)

        request.session['checking_account_balance'] = str(checking_balance)
        request.session['savings_account_balance'] = str(savings_balance)
        request.session['credit_card_account_balance'] = str(credit_card_balance)

        request.session['account_number_checking'] = str(account_number_checking)
        request.session['account_number_savings']  = str(account_number_savings)
        request.session['account_number_credit'] = str(account_number_credit)


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
def checking_acct_page(request, customer_number=1, account_number=1):
    
    if request.user.is_authenticated:
        #obj = checkingAcct.objects.all()

          #find the customer in the Users_bank table
        customer_found = Users_bank.objects.filter(username = request.user)
          #extract the customer id from the found user object.
        customer_found_id = customer_found.first().customer_id

        
        #grab checking account transactions for this customer id 
        customerID = checkingAcct.objects.filter(customer_id = customer_found_id).first() #checkingAcct.objects.first()
        
        
        #account_number = customerID.account_number.account_number

        account_number = Accounts.objects.filter(customer_id = customer_found_id, account_type = 'checking').first().account_number

        # account_balance = Accounts.objects.first().account_balance

        #pull account info for the given customer number and account number
        #checking_info = checkingAcct.objects.filter(customer_id=customer_number, account_number = account_number) #checkingAcct.objects.all()
    
        checking_info = checkingAcct.objects.filter(customer_id=customer_found_id, account_number = account_number)
     
        #balance = checkingAcct.objects.aggregate(balance_sum = Sum('amount'))['balance_sum'] #sums all the amounts and returns the value from the dictionary returned

        balance = checkingAcct.objects.filter(customer_id = customer_found_id).aggregate(balance_sum = Sum('amount'))['balance_sum'] #sums all the amounts and returns the value from the dictionary returned
    
    
     
       # if request.user.is_authenticated:
        account_balance = balance
        current_user = request.user
       # else:
         #    account_balance = 300
          #   current_user = request.user


        context = {
            'checking_posts': checking_info, #checkingAcct.objects.all(),
            'customerID': customer_found_id,#customer_number,#customerID.customer_id.customer_id.customer_id,
            'account_number': account_number,
            'account_balance': account_balance,
            'current_user': current_user,
            'customer_found': customer_found_id #.username
         }

         # return render(request,'main/checking_acct_page.html', context)
        if request.user.is_authenticated:
            return render(request,'main/checking_acct_page.html', context)
        else:
            return render(request,'main/login.html', context)

    return redirect('login')

def creditcard_acct_page(request, customer_number=1, account_number=1):
    
    if request.user.is_authenticated:

          #find the customer in the Users_bank table
        customer_found = Users_bank.objects.filter(username = request.user)
          #extract the customer id from the found user object.
        customer_found_id = customer_found.first().customer_id

        
        #grab checking account transactions for this customer id 
        customerID = credit_cardAcct.objects.filter(customer_id = customer_found_id).first() #credit_cardAcct.objects.first()

        account_number = Accounts.objects.filter(customer_id = customer_found_id, account_type = 'credit_card').first().account_number

        credit_info = credit_cardAcct.objects.filter(customer_id=customer_found_id, account_number = account_number)
     
        balance = credit_cardAcct.objects.filter(customer_id = customer_found_id).aggregate(balance_sum = Sum('amount'))['balance_sum'] #sums all the amounts and returns the value from the dictionary returned
    
    
     
       # if request.user.is_authenticated:
        account_balance = balance
        current_user = request.user
      
        context = {
            'credit_posts': credit_info, #checkingAcct.objects.all(),
            'customerID': customer_found_id,#customer_number,#customerID.customer_id.customer_id.customer_id,
            'account_number': account_number,
            'account_balance': account_balance,
            'current_user': current_user,
            'customer_found': customer_found_id #.username
         }

         # return render(request,'main/checking_acct_page.html', context)
        if request.user.is_authenticated:
            return render(request,'main/creditcard_acct_page.html', context)
        else:
            return render(request,'main/login.html', context)

    return redirect('login')


def savings_acct_page(request, customer_number=1, account_number=1):
    
    if request.user.is_authenticated:

          #find the customer in the Users_bank table
        customer_found = Users_bank.objects.filter(username = request.user)
          #extract the customer id from the found user object.
        customer_found_id = customer_found.first().customer_id

        
        #grab checking account transactions for this customer id 
        customerID = savingsAcct.objects.filter(customer_id = customer_found_id).first() 

        account_number = Accounts.objects.filter(customer_id = customer_found_id, account_type = 'savings').first().account_number

        savings_info = savingsAcct.objects.filter(customer_id=customer_found_id, account_number = account_number)
     
        balance = savingsAcct.objects.filter(customer_id = customer_found_id).aggregate(balance_sum = Sum('amount'))['balance_sum'] #sums all the amounts and returns the value from the dictionary returned
    
    
     
       # if request.user.is_authenticated:
        account_balance = balance
        current_user = request.user
      
        context = {
            'savings_posts': savings_info, #checkingAcct.objects.all(),
            'customerID': customer_found_id,#customer_number,#customerID.customer_id.customer_id.customer_id,
            'account_number': account_number,
            'account_balance': account_balance,
            'current_user': current_user,
            'customer_found': customer_found_id #.username
         }

         # return render(request,'main/checking_acct_page.html', context)
        if request.user.is_authenticated:
            return render(request,'main/savings_acct_page.html', context)
        else:
            return render(request,'main/login.html', context)

    return redirect('login')

def profile_view(request):
    if request.user.is_authenticated:
         
         #find the customer in the Users_bank table
        customer_found = Users_bank.objects.filter(username = request.user)
          #extract the customer id from the found user object.
        customer_found_id = customer_found.first().customer_id

        customer_info = Customers_List.objects.filter(customer_id = customer_found_id).first() #checkingAcct.objects.first()

    
        context = {
            'username' : request.user,
            'customer_info' : customer_info,
        }
        return render(request, 'main/profile.html', context)
    else:
        return redirect('login')

def profile_edit_view(request):
    if request.user.is_authenticated:

        customer_found = Users_bank.objects.filter(username = request.user)
        customer_found_id = customer_found.first().customer_id
        customer_info = Customers_List.objects.filter(customer_id = customer_found_id).first()

        user_id = Customers_List.objects.get(pk=customer_info.id) #current session instance to get current user

        if request.method == 'POST':
            form = Profile_Edit_Form(request.POST, instance=user_id)

            if form.is_valid():
                form.save()
                messages.success(request, f'Your profile information was updated.')
                return redirect('profile')

        else:
            data = {
               # 'id' : customer_info.id,
                'customer_id': customer_found_id,
                'first_name': customer_info.first_name,
                'middle_name': customer_info.middle_name,
                'last_name' : customer_info.last_name,
                'address': customer_info.address,
                'city' : customer_info.city,
                'state' : customer_info.state,
                'zipcode': customer_info.zipcode,
                'phone_number': customer_info.phone_number
                }
            form = Profile_Edit_Form(data)
            args = {'form': form}
            return render(request, 'main/profile_edit.html', args)
        #return redirect('login')
    else:
        return redirect('login')


def account_summary(request):
    return render(request, 'main/account_summary.html')
       