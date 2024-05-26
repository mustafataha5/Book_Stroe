from django.urls import path,include
from . import views 

app_name = 'app'


urlpatterns = [
    path('',views.index , name = 'index'),
    path('login',views.login,name='login')
    path('register',views.register, name='register'),
    path('login',views.login), 
    path('create_user',views.create_user), 
    
]