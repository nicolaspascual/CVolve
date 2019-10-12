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


def get_experience_sorted_by_distance(user_id, offer_id):
    return UserExperience.objects.raw(
        f"""
        SELECT main_userexperience.*
        FROM ((main_user INNER JOIN main_userexperience ON main_user.user_ptr_id = main_userexperience.user_id)
                INNER JOIN main_jobofferexperiencedistance on main_userexperience.id = main_jobofferexperiencedistance.experience_id)
                INNER JOIN main_joboffer on main_joboffer.id = main_jobofferexperiencedistance.job_offer_id
        WHERE main_user.user_ptr_id={user_id} and main_joboffer.id = {offer_id}
        ORDER BY main_jobofferexperiencedistance.distance
        """
    )
