from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogItems(models.Model):
    """single blog"""
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=None)
    content = models.CharField(max_length=800)
    date_added = models.DateField(auto_now_add=True)
    is_del = models.IntegerField(default=0)

    def __str__(self):
        return "myblog:"+self.title
