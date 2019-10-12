from django.db import models
from .user import User
from .job_offer import JobOffer

class JobOfferDistance(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    distance = models.FloatField('Distance')

    class Meta:
        verbose_name_plural = 'JobOfferDistances'