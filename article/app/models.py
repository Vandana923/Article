from django.db import models


# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=62)
    desc = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title
