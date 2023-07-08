from django.contrib import admin

# Register your models here.

from blog1_app.models import Post

admin.site.register(Post)