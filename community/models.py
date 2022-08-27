from django.db import models
from django.contrib.auth import get_user_model

# 3rd party
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField

# Photoshare model for the community app
class Photoshare(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    tags = TaggableManager()
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # Method for how each job will display in the admin area
    def __str__(self):
        return self.title