from django.db import models
from .user import User

class UserEducation(models.Model):

    title = models.CharField('Title', max_length=150)
    institution = models.CharField('Institution', max_length=150)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date', blank=True, null=True)
    summary = models.TextField('Summary')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'UserEducations'

    def to_comparable_text(self):
        return ' '.join([
            self.title, self.summary
        ])


def get_education_sorted_by_distance(user_id, offer_id):
    return UserEducation.objects.raw(
        f"""
        SELECT main_usereducation.*
        FROM ((main_user INNER JOIN main_usereducation ON main_user.user_ptr_id = main_usereducation.user_id)
                INNER JOIN main_joboffereducationdistance on main_usereducation.id = main_joboffereducationdistance.education_id)
                INNER JOIN main_joboffer on main_joboffer.id = main_joboffereducationdistance.job_offer_id
        WHERE main_user.user_ptr_id={user_id} and main_joboffer.id = {offer_id}
        ORDER BY main_joboffereducationdistance.distance
        """
    )