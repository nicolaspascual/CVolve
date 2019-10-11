from django.http import HttpResponse
from django.views import View


class ExampleView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('This is an example')
