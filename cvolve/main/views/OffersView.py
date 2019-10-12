from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from cvolve.main import models


class OffersView(View):
    
    def get(self, request):
        user = models.User.objects.get(pk=request.user.id)
        offers = user.get_offers_sorted_by_distance(return_distances=True)

        return render(request, 'offers.html', {
            'offers': offers
        })
