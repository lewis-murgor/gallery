from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


