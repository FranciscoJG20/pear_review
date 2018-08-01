from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Pear(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    photo_url = models.TextField(blank=True)


class Issue(models.Model):
    title = models.CharField(max_length=100 , blank=True)
    body = models.TextField(blank=True)
    screenshot_url = models.TextField(blank=True)
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    ISSUE_STATUS_OPTIONS = (
        ('OPEN', 'OPEN'),
        ('CLOSED', 'CLOSED')
    )
    issue_status = models.CharField(
        max_length=6,
        choices=ISSUE_STATUS_OPTIONS,
        default = OPEN,
    )

    def __str__(self):
        return self.title 

    # ^^^ This method defines what an instance of the model will show up as by default. 
    # It will be really helpful for debugging in the future!

class Comment(models.Model):
    content = models.TextField(blank=True)
    author = models.CharField(max_length=200)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author  