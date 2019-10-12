from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.views import View
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

from cvolve.main.models import (JobOffer, User, get_education_sorted_by_distance,
                                get_experience_sorted_by_distance,
                                get_projects_sorted_by_distance, get_skills_sorted_by_distance)


class CVDownloadView(View):

    def get(self, request, offer_id, cv_color):
        user = User.objects.get(pk=request.user.id)
        offer = JobOffer.objects.get(pk=offer_id)

        response = HttpResponse(content_type='application/pdf')
        html = render_to_string('pdf_cv.html', {
            'user': user, 'offer': offer,
            'educations': get_education_sorted_by_distance(user.id, offer.id, 2, True),
            'experiences': get_experience_sorted_by_distance(user.id, offer.id, 2, True),
            'projects': get_projects_sorted_by_distance(user.id, offer.id, 2, True),
            'skills': get_skills_sorted_by_distance(user.id, offer.id, return_distances=True),
            'cv_color': cv_color
        })

        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response
