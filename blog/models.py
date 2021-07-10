from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Post model and user Model are related(one to many relation)
from django.urls import reverse
# Create your models here.

class Post(models.Model): #Going to inherit from models.Model
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)  #argument to be passed in related table, on cascade, if a user is deleted, delete their posts as well, author = user(object), not username

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) #returns full path as a string
