from django.db import models
from .user import User

class UserEducation(models.Model):

    title = models.CharField('Title', max_length=150)
    institution = models.CharField('Institution', max_length=150)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date', blank=True)
    summary = models.TextField('Summary')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'UserEducations'
