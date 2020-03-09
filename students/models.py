from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):

    choices = (
        ('ADHD', 'ADHD'),
        ('DSL', 'Dyslexia'),
        ('DEM', 'Dementia')
    )
    username = models.CharField(max_length=50, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    disabilty = models.CharField(choices=choices, max_length=10)
    time = models.TimeField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return "{}".format(self.email)