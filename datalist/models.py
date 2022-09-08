from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    line = models.CharField(max_length=100, default='text-decoration-none')
    
    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.name
