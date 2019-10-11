from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class ExampleView(View):
    
    def get(self, request):
        # <view logic>
        return render(request, 'test_template.html')
