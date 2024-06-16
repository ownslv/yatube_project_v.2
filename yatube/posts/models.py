from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    tittle = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.tittle


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='posts',
    )
