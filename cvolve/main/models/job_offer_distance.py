from math import exp

from django.db import models

from .job_offer import JobOffer
from .user import User


class JobOfferDistance(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    distance = models.FloatField('Distance')

    class Meta:
        verbose_name_plural = 'JobOfferDistances'
        unique_together = (('user', 'job_offer'),)
