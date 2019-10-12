from django.db import models


class JobOffer(models.Model):
    title = models.CharField('Title', max_length=120)
    description = models.TextField('Description')

    responsabilities = models.TextField('Responsabilities')
    minimun_requirements = models.TextField('Minimun Requirements')
    preferred_requirements = models.TextField('Preferred Requirements', blank=True)

    type = models.CharField('Type', max_length=80)
    compensation = models.FloatField('Compensation', blank=True)
    duration = models.IntegerField('Duration', blank=True)
    duration_unit = models.CharField('Duration Unit', max_length=20, blank=True)

    company = models.CharField('Company', max_length=120)
    department = models.CharField('Department', max_length=120)

    city = models.CharField('City', max_length=120)
    state = models.CharField('State', max_length=120)
    country = models.CharField('Country', max_length=120)

    class Meta:
        verbose_name_plural = 'JobOffers'
