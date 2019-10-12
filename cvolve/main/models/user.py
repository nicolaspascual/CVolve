from django.contrib.auth.models import User as DjangoUser
from django.db import models

from .job_offer import JobOffer

class User(DjangoUser):

    name = models.CharField('Name', max_length=50)
    surnames = models.CharField('Surnames', max_length=150)
    mail = models.CharField('Mail', max_length=50)
    phone = models.CharField('Phone', max_length=50)
    summary = models.TextField('Summary')
    languages = models.TextField('Languages')  # Separated by new lines

    @property
    def skills(self):
        return self.userskill_set.all()

    @property
    def experience(self):
        return self.userexperience_set.all()

    @property
    def projects(self):
        return self.userprojects_set.all()

    @property
    def education(self):
        return self.usereducation_set.all()

    def get_offers_sorted_by_distance(self, return_distances=False):
        distance_clause = ", main_jobofferdistance.distance" if return_distances else ''
        return JobOffer.objects.raw(
            f"""
            SELECT main_joboffer.* {distance_clause}
            FROM (main_user INNER JOIN main_jobofferdistance ON main_user.user_ptr_id = main_jobofferdistance.user_id)
                INNER JOIN main_joboffer ON main_jobofferdistance.job_offer_id = main_joboffer.id
            WHERE main_user.user_ptr_id={self.id}
            ORDER BY main_jobofferdistance.distance
            """
        )

    def to_comparable_text(self):
        return ' '.join([
            self.summary, self.languages,
            ' '.join(exp.to_comparable_text() for exp in self.skills),
            ' '.join(exp.to_comparable_text() for exp in self.experience),
            ' '.join(proj.to_comparable_text() for proj in self.projects),
            ' '.join(ed.to_comparable_text() for ed in self.projects)
        ])
