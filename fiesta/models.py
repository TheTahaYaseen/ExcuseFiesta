from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="media/profile_pics/", blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return self.associated_user.username
    
class ExcuseCategory(models.Model):
    name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Excuse(models.Model):
    content = models.CharField()
    category = models.ForeignKey(ExcuseCategory, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
