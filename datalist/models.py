from django.db import models
from django.contrib.auth.models import User

# class Username(models.Model):
#     name = models.CharField(max_length=100)
#     password1 = models.CharField(max_length=100)
#     password2 = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Usertask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    line = models.CharField(max_length=100, default='text-decoration-none')
    
    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.name
