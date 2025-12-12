from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.



class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    

    def __str__(self):
        return self.username
    
class Award(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='awards/icons/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class UserAward(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="awards"
    )
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'award')

    def __str__(self):
        return f"{self.user.username} → {self.award.title}"