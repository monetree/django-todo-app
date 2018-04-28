from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)

    def __str__(self):
        return '%s'%self.name








