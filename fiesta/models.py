from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="media/profile_pics/", blank=True, null=True)

    def __repr__(self) -> str:
        return self.associated_user.username