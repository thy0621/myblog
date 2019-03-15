from django.contrib import admin

# Register your models here.

# username:admin  password: 123
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','content','pub_time')
    list_filter = ('pub_time',)
admin.site.register(Article,ArticleAdmin)