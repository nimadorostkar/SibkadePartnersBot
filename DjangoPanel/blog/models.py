from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return str(self.name)



class Post(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='media/blog_cover',null=True,blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.title