from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from cvolve.main import models


class OffersView(View):
    
    def get(self, request):
        offers = models.JobOffer.objects.all()

        return render(request, 'offers.html', {
            'offers': offers
        })
