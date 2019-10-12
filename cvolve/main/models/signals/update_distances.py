from django.db.models.signals import post_save
from django.dispatch import receiver

from cvolve.main.models import (User, UserEducation, UserExperience, JobOffer,
                                UserProjects, UserSkill, JobOfferDistance,
                                JobOfferEducationDistance, JobOfferExperienceDistance,
                                JobOfferSkillDistance, JobOfferProjectsDistance)
from cvolve.main.services import calculate_document_distance


@receiver(post_save, sender=User, dispatch_uid='Update distance of user')
def update_user_distance(sender, instance, **kwargs):
    for job_offer in JobOffer.objects.all():
        JobOfferDistance(
            user=instance,
            job_offer=job_offer,
            distance=calculate_document_distance(
                instance.to_comparable_text(),
                job_offer.to_comparable_text()
            )
        ).save()


@receiver(post_save, sender=UserEducation, dispatch_uid='Update distance of user education')
def update_user_distance_education(sender, instance, **kwargs):
    for job_offer in JobOffer.objects.all():
        JobOfferEducationDistance(
            education=instance,
            job_offer=job_offer,
            distance=calculate_document_distance(
                instance.to_comparable_text(),
                job_offer.to_comparable_text()
            )
        ).save()


@receiver(post_save, sender=UserExperience, dispatch_uid='Update distance of user experience')
def update_user_distance_experience(sender, instance, **kwargs):
    for job_offer in JobOffer.objects.all():
        JobOfferExperienceDistance(
            experience=instance,
            job_offer=job_offer,
            distance=calculate_document_distance(
                instance.to_comparable_text(),
                job_offer.to_comparable_text()
            )
        ).save()


@receiver(post_save, sender=UserProjects, dispatch_uid='Update distance of user projects')
def update_user_distance_projects(sender, instance, **kwargs):
    for job_offer in JobOffer.objects.all():
        JobOfferProjectsDistance(
            projects=instance,
            job_offer=job_offer,
            distance=calculate_document_distance(
                instance.to_comparable_text(),
                job_offer.to_comparable_text()
            )
        ).save()


@receiver(post_save, sender=UserSkill, dispatch_uid='Update distance of user skill')
def update_user_distance_skill(sender, instance, **kwargs):
    for job_offer in JobOffer.objects.all():
        JobOfferSkillDistance(
            skill=instance,
            job_offer=job_offer,
            distance=calculate_document_distance(
                instance.to_comparable_text(),
                job_offer.to_comparable_text()
            )
        ).save()


@receiver(post_save, sender=JobOffer, dispatch_uid='Update distance of job offer')
def update_job_offer_distance(sender, instance, **kwargs):
    for user in User.objects.all():
        JobOfferDistance(
            user=user,
            job_offer=instance,
            distance=calculate_document_distance(
                instance.to_comparable_text(),
                user.to_comparable_text()
            )
        ).save()

        for education in user.education:
            JobOfferEducationDistance(
                education=education,
                job_offer=instance,
                distance=calculate_document_distance(
                    instance.to_comparable_text(),
                    education.to_comparable_text()
                )
            ).save()

        for experience in user.experience:
            JobOfferExperienceDistance(
                experience=experience,
                job_offer=instance,
                distance=calculate_document_distance(
                    instance.to_comparable_text(),
                    education.to_comparable_text()
                )
            ).save()
        
        for project in user.projects:
            JobOfferProjectsDistance(
                projects=project,
                job_offer=instance,
                distance=calculate_document_distance(
                    instance.to_comparable_text(),
                    project.to_comparable_text()
                )
            ).save()

        for skill in user.skills:
            JobOfferSkillDistance(
                skill=skill,
                job_offer=instance,
                distance=calculate_document_distance(
                    instance.to_comparable_text(),
                    skill.to_comparable_text()
                )
            ).save()