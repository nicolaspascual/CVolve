from django.db import models
from .user import User

class UserProjects(models.Model):
    name = models.CharField('Name', max_length=120)
    summary = models.TextField('Summary')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'UserProjects'


    def to_comparable_text(self):
        return ' '.join([
            self.name, self.summary
        ])


def get_projects_sorted_by_distance(user_id, offer_id, limit=None, return_distances=False):
    limit_clause = f'LIMIT {limit}' if limit else ''
    distance_clause = ", main_jobofferprojectsdistance.distance" if return_distances else ''
    return UserProjects.objects.raw(
        f"""
        SELECT main_userprojects.* {distance_clause}
        FROM ((main_user INNER JOIN main_userprojects ON main_user.user_ptr_id = main_userprojects.user_id)
                INNER JOIN main_jobofferprojectsdistance on main_userprojects.id = main_jobofferprojectsdistance.projects_id)
                INNER JOIN main_joboffer on main_joboffer.id = main_jobofferprojectsdistance.job_offer_id
        WHERE main_user.user_ptr_id={user_id} and main_joboffer.id = {offer_id}
        ORDER BY main_jobofferprojectsdistance.distance
        {limit_clause}
        """
    )
