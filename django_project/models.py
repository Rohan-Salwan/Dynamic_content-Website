from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField, TextField

# Create your models here.
class exp(models.Model):
    name=CharField(max_length=100)
    des=TextField()
    price=IntegerField()
    available=BooleanField(default=False)
    img=models.ImageField(upload_to='pics')
