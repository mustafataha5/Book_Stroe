from django.shortcuts import render , redirect
from .models import User
from  django.contrib import messages
import bcrypt
import datetime
# Create your views here.

def index (request): 
    return render(request,'user_main_page.html') 




def register(request): 
    return render(request,'registeration.html')
    
    
def login(request):
    return render(request,'login.html')
 
 
 
def create_user(request): 
    
    if request.method == 'POST': 
        errors = User.objects.user_validation(request.POST)
        if len(errors) > 0 : 
            for key,val in  errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('app:register')
        
        user_fname = request.Post['first_name']
        user_lname = request.Post['last_name']
        user_email = request.POST['email']
        password =bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
        brithday =  datetime.datetime.strptime(request.POST['birthday'],'').date()
        gender = request.POST['gender']
        user = User.objects.create(first_name=user_fname,last_name=user_lname,gender=gender,brithday=brithday,password=password)
           
    
    





