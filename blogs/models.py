from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE, related_name='posts',
        null=False,
        blank=False
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return f'{self.title} by {self.author.first_name} {self.author.last_name}'


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='comments'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='comments'
    )
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    def __str__(self) -> str:
        return f'{self.author.first_name} {self.author.last_name} to {self.post.title} '
