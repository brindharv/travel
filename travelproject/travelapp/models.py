from django.db import models

# Create your models here.
class travel(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()

    def __str__(self):
        return self.name


