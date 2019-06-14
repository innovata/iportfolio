
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Project(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=64)
    giturl = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='classification')

    def __str__(self):
        return f"{self.id} - {self.name}"

class Coworker(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    projects = models.ManyToManyField(Project, blank=True, related_name="coworkers")

    def __str__(self):
        return f"{self.surname} {self.name}"
