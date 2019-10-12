from django.db import models
from .user_experience import UserExperience
from .job_offer import JobOffer

class JobOfferExperienceDistance(models.Model):

    experience = models.ForeignKey(UserExperience, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    distance = models.FloatField('Distance')

    class Meta:
        verbose_name_plural = 'JobOfferExperienceDistances'