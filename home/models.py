from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    image = models.ImageField(upload_to='/workspace/pp4-photography-website/images/')