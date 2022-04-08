from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    dish = models.CharField(
        max_length=20, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # card = models.TextField()
    card = RichTextField(blank=True, null=True)
    date_stamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

