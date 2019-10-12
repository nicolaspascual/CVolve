from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class TypeFormView(View):
    
    def get(self, request):
        # <view logic>
        return render(request, 'typeform_template.html')
