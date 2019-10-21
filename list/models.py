from django.db import models
from datetime import datetime, date

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=False, auto_now= False , blank=True)
    

    def __str__(self):
        return self.item 
  