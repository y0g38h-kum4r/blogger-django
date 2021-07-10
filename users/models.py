from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs): #method that is run after the model is saved, method that already exists in parent class
    #     super().save(*args, **kwargs) #overriding the save methods of model
    #
    #     img = Image.open(self.image.path) #opens the image of the current instance
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
# Create your models here.
