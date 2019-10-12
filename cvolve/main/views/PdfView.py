from django.views import View
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


class PdfView(View):
    
    def get(self, request):
        # <view logic>
        return self.render_to_pdf('pdf_cv.html')

    def render_to_pdf(self, template_src, context_dict={}):
        template = get_template(template_src)
        html = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return HttpResponse('There was an error on the PDF generation')
