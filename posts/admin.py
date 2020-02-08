from django.contrib import admin
from posts.models import Post,Comment, Feed
# Register your models here.
admin.site.register(Post)
admin.site.register(Feed)
admin.site.register(Comment)