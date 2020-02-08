from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_image', height_field=None, width_field=None, max_length=100, default="Sorry")
    # people = models.CharField(max_length=300, default="None")
    likes = models.IntegerField(default=0)
    post_date = models.DateField(auto_now=False, auto_now_add= False, default =timezone.now)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-post_date']

class Feed(models.Model):
    name = models.CharField(max_length=80)
    no_of_followers = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete= models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)