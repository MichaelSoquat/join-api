from django.db import models
from datetime import date

# Create your models here.
sizes = [('xl','xl'),
('l','l'),
('s','s')]
class Test(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    size_options = models.CharField(max_length=256, choices=sizes)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    category= models.CharField(max_length=128)
    description= models.CharField(max_length=128)
    dueDate= models.DateField(default=date.today)
    title= models.CharField(max_length=128)
    urgency= models.CharField(max_length=128)
    status= models.CharField(max_length=128)

    def __str__(self) -> str:
        return '{0}'.format(self.title)


