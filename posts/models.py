from django.db import models
from accounts.models import Owner


# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='post_owner')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.IntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.owner.username


class Comment(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='comment_owner')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_owner')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username
