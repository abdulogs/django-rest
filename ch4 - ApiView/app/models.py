from django.db import models

class Student(models.Model):
    fullname = models.CharField(
        max_length=200, null=True, blank=True, default="")
    email = models.CharField(max_length=200, null=True, blank=True, default="")
    phone = models.CharField(max_length=200, null=True, blank=True, default="")
