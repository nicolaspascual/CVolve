from django.db import models
from .user_skill import UserSkill
from .job_offer import JobOffer

class JobOfferSkillDistance(models.Model):

    skill = models.ForeignKey(UserSkill, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    distance = models.FloatField('Distance')

    class Meta:
        verbose_name_plural = 'JobOfferSkillDistances'