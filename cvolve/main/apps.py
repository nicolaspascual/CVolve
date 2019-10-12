from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'cvolve.main'

    def ready(self):
        from cvolve.main.models.signals.update_distances import (
            update_user_distance, update_user_distance_education, 
            update_user_distance_experience, update_user_distance_projects,
            update_user_distance_skill, update_job_offer_distance
        )
