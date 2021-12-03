from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
