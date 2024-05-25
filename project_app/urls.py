from django.urls import path,include
from . import views 

app_name = 'our_app'


urlpatterns = [
    path('',views.index , name = 'index'),
    path('register',views.register),
    path('login',views.login), 
    path('create_user',views.create_user), 
    
]