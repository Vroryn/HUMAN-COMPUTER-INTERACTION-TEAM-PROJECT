from django.contrib import admin

#added by rene
from .models import Users
from .models import Customers 
from .models import Customers_List
from .models import Accounts
from .models import checkingAcct
# Register your models here.


#added by rene
admin.site.register(Users)
admin.site.register(Customers)
admin.site.register(Customers_List)
admin.site.register(Accounts)
admin.site.register(checkingAcct)