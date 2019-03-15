from django.contrib import admin

# Register your models here.

# username:admin  password: 123
from .models import Article

admin.site.register(Article)