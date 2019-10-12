from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from cvolve.main import models


class OfferDetailView(View):
    
    def get(self, request, id):
        offer = models.JobOffer.objects.get(pk=id)
        distance = models.JobOfferDistance.objects.get(user_id=request.user.id, job_offer=offer)

        return render(request, 'offer_detail.html', {
            'offer': offer, 'distance': distance.distance
        })
