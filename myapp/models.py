from django.db import models

# Create your models here.

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='employee_images/')

    def __str__(self):
        return self.name
