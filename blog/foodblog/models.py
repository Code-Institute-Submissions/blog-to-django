from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    dish = models.CharField(max_length=20, null=False, blank=False, default='dish') 
    # dish = models.CharField(max_length=20, null=False, blank=False, default=title[0:5]) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')