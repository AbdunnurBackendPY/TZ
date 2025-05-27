from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username


class Daily_planner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=100)
    heading = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.heading
