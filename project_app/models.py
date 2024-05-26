from django.db import models
import datetime

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
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CategoryManger()


class Language(models.Model):
    name = models.CharField(max_length=45)
    objects = LanguageManger()
    
class Author(models.Model): 
    first_name = models.CharField(max_length=45,default=' ')
    last_name = models.CharField(max_length=45,default=' ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
class Book(models.Model): 
    title = models.CharField(max_length=45)
    description = models.TextField()
    number_of_pages = models.IntegerField()
    url_image = models.TextField()
    price = models.FloatField()
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='books', on_delete=models.CASCADE)
    liked_by_users= models.ManyToManyField(User,related_name='likes_books',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()



class Order(models.Model):
    confirm_buy = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books= models.ManyToManyField(Book,related_name='orders')
    objects = OrderManger()
    
class Review (models.Model): 
    users = models.ForeignKey(User,related_name='reviews', on_delete=models.CASCADE)
    books = models.ForeignKey(Book,related_name='reviews', on_delete=models.CASCADE) 
    review_level = models.IntegerField()
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   











