from django.contrib import admin
from forum.models import Category, Post, Reply, Comment,UserProfile

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Comment)
admin.site.register(UserProfile)
