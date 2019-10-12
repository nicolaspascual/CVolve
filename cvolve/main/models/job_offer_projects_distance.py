from django.db import models
from .user_projects import UserProjects
from .job_offer import JobOffer

class JobOfferProjectsDistance(models.Model):

    projects = models.ForeignKey(UserProjects, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    distance = models.FloatField('Distance')

    class Meta:
        verbose_name_plural = 'JobOfferProjectsDistances'
        unique_together = (('projects', 'job_offer'),)
