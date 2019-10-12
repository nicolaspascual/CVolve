from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from cvolve.main import models


class OffersView(View):
    
    def get(self, request):
        user = models.User.objects.get(pk=request.user.id)
        offers = user.get_offers_sorted_by_distance(return_distances=True)
        first_offer = offers[0]
        other_offers = [o for o in offers if o.id != first_offer.id]

        return render(request, 'offers.html', {
            'first_offer': first_offer,
            'offers': other_offers
        })
