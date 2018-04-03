from django.db import models
from django.utils import timezone

#Create your models here
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    categories = models.ManyToManyField(Category)
    attachments = models.ManyToManyField(Attachment)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    published_date = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
