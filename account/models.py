from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# from django.db.models.signals import post_save
# from django.dispatch import receiver
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
    image   = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
        

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name ="owner", null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend,created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)
    
    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user= current_user
        )
        friend.users.remove(new_friend)

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=User) 