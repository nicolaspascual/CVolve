from django.views import View
from django.shortcuts import redirect, reverse


class MainView(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('offers'))
        else:
            return redirect(reverse('login'))
