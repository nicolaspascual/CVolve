from django.contrib.auth.models import User as DjangoUser
from django.db import models

class User(DjangoUser):

    name = models.CharField('Name', max_length=50)
    surnames = models.CharField('Surnames', max_length=150)
    mail = models.CharField('Mail', max_length=50)
    phone = models.CharField('Phone', max_length=50)
    summary = models.TextField('Summary')
    skills = models.TextField('Skills') # Separated by new lines
    languages = models.TextField('Languages') # Separated by new lines

