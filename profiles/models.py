from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='profile'
    )
    bio = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.get_username()
