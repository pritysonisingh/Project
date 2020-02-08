from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# class Feed(models.Model):
#     name = models.CharField(max_length=80)
#     no_of_followers = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name

class Profile(models.Model):
    name    = models.CharField(max_length=80)
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200)
    bio     = models.CharField(max_length=150, blank=True, null=True)
    dob     = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=User) 