from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=500)
    twitter_link = models.URLField(max_length=500)
    instagram_link = models.URLField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name