from django.contrib import admin

# Register your models here.
from .models import Comment
from kk.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'nickname', 'content', 'website', 'created_time')