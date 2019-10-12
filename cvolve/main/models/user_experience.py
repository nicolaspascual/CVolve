from django.db import models
from .user import User

class UserExperience(models.Model):

    role = models.CharField('Role', max_length=150)
    company = models.CharField('Company', max_length=150)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date', blank=True, null=True)
    summary = models.TextField('Summary')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'UserExperiences'

    def to_comparable_text(self):
        return ' '.join([
            self.role, self.summary
        ])