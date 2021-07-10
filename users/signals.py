from django.db.models.signals import post_save #this is the signal which gets fired when the object is saved, need a post_save signal when a user is created
from django.contrib.auth.models import User #built in User model, sender
from django.dispatch import receiver #gets the signal and performs some tasks
from .models import Profile #will be creating a profile in function

#we want a user profile to be created for each new user

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): #we want this function to run every time a user is created, creates all of the arguments, that post_save signal passed to it!, one is the instance of the User and other is created status
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #saves profile every time user pbject is saved
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
