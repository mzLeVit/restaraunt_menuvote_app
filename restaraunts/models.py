from django.db import models
from django.contrib.auth.models import User



class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.JSONField()


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'choice')  # Користувач може голосувати один раз на варіант