from django.contrib import admin
from .models import User, UserToken, Question


# Register your models here.
@admin.register(User)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'u_name', 'is_super')


@admin.register(UserToken)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'u_name', 'u_token')


@admin.register(Question)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'u_name', 'title')
