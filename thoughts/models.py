from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Thought(models.Model):
    STATUS = (
        ('0', 'Visible'),
        ('1', 'Pending'),
        ('2', 'Deleted by Author'),
        ('3', 'Delted by Mods'),
    )

    content = models.CharField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymous = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS, default = '0')
    date_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    STATUS = (
        ('0', 'Visible'),
        ('1', 'Pending'),
        ('2', 'Deleted by Author'),
        ('3', 'Delted by Mods'),
    )

    content = models.CharField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    anonymous = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS, default = '0')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    linked_post = models.ForeignKey(Thought, on_delete=models.CASCADE, null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)

class Anonymous_Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    linked_post = models.ForeignKey(Thought, on_delete=models.CASCADE, null=True, blank=True)
    anonymous_name = models.CharField(max_length=3000, default="", null=False, blank=False)