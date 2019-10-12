from django.db import models
from .user import User

class UserSkill(models.Model):

    name = models.CharField('Name', max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'UserSkills'

    def to_comparable_text(self):
        return self.name


def get_skills_sorted_by_distance(user_id, offer_id):
    return UserSkill.objects.raw(
        f"""
        SELECT main_userskill.*
        FROM ((main_user INNER JOIN main_userskill ON main_user.user_ptr_id = main_userskill.user_id)
                INNER JOIN main_jobofferskilldistance on main_userskill.id = main_jobofferskilldistance.skill_id)
                INNER JOIN main_joboffer on main_joboffer.id = main_jobofferskilldistance.job_offer_id
        WHERE main_user.user_ptr_id={user_id} and main_joboffer.id = {offer_id}
        ORDER BY main_jobofferskilldistance.distance
        """
    )