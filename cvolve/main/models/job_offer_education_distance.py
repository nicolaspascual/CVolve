from django.db import models
from .user_education import UserEducation
from .job_offer import JobOffer


class JobOfferEducationDistance(models.Model):

    education = models.ForeignKey(UserEducation, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    distance = models.FloatField('Distance')

    class Meta:
        verbose_name_plural = 'JobOfferEducationDistance'
        unique_together = (('education', 'job_offer'),)
