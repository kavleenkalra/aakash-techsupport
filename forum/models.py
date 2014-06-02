from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
#from django.db.models.signals import post_save

class UserProfile(models.Model):
    #avatar = ImageField("Profile Pic", upload_to="avatar", blank=True, null=True)
    posts = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)
    user =models.OneToOneField(User, related_name="profile")

    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=500)

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse2("forum", dpk=self.pk)


class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField()
    category = models.ForeignKey(Category, related_name="posts")
    vote = models.IntegerField(default=0)
    
    
    class Meta:
        ordering = ["created"]

    def __unicode__(self):
        return (self.title)

class Reply(models.Model):
    title = models.ForeignKey(Post, related_name="post")
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField()
    vote = models.IntegerField(default=0)


    class Meta:
        ordering = ["created"]

    def __unicode__(self):
        return (self.body)


class Comment(models.Model):
    comment = models.ForeignKey(Reply)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    vote = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
    	return self.body

