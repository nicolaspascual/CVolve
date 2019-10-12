from django.db import models
from .user import User

class UserProjects(models.Model):
    name = models.CharField('Name', max_length=120)
    summary = models.TextField('Summary')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'UserProjects'

