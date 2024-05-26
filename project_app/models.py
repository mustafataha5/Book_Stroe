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


class CommentManger(models.Manager):
    def user_validation(self,postData): 
        errors = {}
        
        
        
        return errors  
    

class CategoryManger(models.Manager):
    def category_validation(self,postData): 
        errors = {}
        
        
        
        return errors  
    

class LanguageManger(models.Manager):
    def Language_validation(self,postData): 
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



class Category(models.Model):
    name = models.CharField(max=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CategoryManger()


class Language(models.Model):
    name = models.CharField(max=45)
    objects = LanguageManger()
    

class Book(models.Model): 
    title = models.CharField(max=45)
    description = models.TextField()
    number_of_pages = models.CharField(max=20)
    url_image = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()










