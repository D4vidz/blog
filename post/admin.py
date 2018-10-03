from django.contrib import admin
from post.models import Tag, Blog, Comment

# Register your models here.

admin.site.register(Tag),
admin.site.register(Blog),
admin.site.register(Comment)
