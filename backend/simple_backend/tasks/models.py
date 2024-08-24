
from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

