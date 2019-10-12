from django.views import View
from django.shortcuts import render

from cvolve.main.models import (JobOffer, User, get_education_sorted_by_distance,
                                get_experience_sorted_by_distance,
                                get_projects_sorted_by_distance, get_skills_sorted_by_distance)


class CVPreviewView(View):

    def get(self, request, offer_id):
        user = User.objects.get(pk=request.user.id)
        offer = JobOffer.objects.get(pk=offer_id)

        return render(request, 'cv_preview.html', {
            'user': user, 'offer': offer,
            'educations': get_education_sorted_by_distance(user.id, offer.id,
                                                           return_distances=True),
            'experiences': get_experience_sorted_by_distance(user.id, offer.id,
                                                             return_distances=True),
            'projects': get_projects_sorted_by_distance(user.id, offer.id,
                                                        return_distances=True),
            'skills': get_skills_sorted_by_distance(user.id, offer.id,
                                                    return_distances=True),
        })
