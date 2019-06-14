
from django.db import models

# Create your models here.



class Node(models.Model):
    name = models.CharField(max_length=50)
    group = models.IntegerField(default=0)
    category = models.CharField(max_length=20)
    lang = models.CharField(max_length=20)

    def __str__(self):
        return f" id:[{self.id}] - {self.name} | {self.group} | {self.category} | {self.lang}"

class Link(models.Model):
    source = models.CharField(max_length=64)
    target = models.CharField(max_length=64)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f" id:[{self.id}] - {self.source} | {self.target} | {self.value}"
