from django.db import models

# Create your models here.
class Data(models.Model):
    x_value = models.IntegerField(default=0)
    y_value = models.IntegerField(default=0)

    
    
