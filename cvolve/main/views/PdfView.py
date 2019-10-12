from django.views import View

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration


class PdfView(View):
    
    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        html = render_to_string('pdf_cv.html', {})

        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response
