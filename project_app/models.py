from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def user_validation(self,postData): 
        errors = {}
        
        
        
        return errors

class PostManager(models.Manager):
    def user_validation(self,postData): 
        errors = {}
        
        
        
        return errors 
        


class BookManager(models.Manager):
    def Book_validation(self,postData): 
        errors = {}
        
        
        
        return errors

class OrderManger(models.Manager):
    def user_validation(self,postData): 
        errors = {}
        
        
        
        return errors   


class CommentManger(models.Manager):
    def user_validation(self,postData): 
        errors = {}
        
        
        
        return errors  


class User(models.Model): 
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=64)
    birthday = models.DateField(null=True)
    gender = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class Author(models.Model): 
    user = models.OneToOneField(User,on_delete=models.CASCADE)     

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    objects = PostManager()





class Comment(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    objects = CommentManger()


class Order(models.Model):
    confirm_buy = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderManger()

    



class Book(models.Model): 
    title = models.CharField(max=45)
    description = models.TextField()
    number_of_pages = models.CharField(max=20)
    url_image = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()







