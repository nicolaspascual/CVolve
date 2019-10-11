from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

class RegisterView(View):
    
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.POST.get('password') == request.POST.get('repeat_password'):
            user = User.objects.create_user(
                request.POST.get('username'),
                password=request.POST.get('password')
            )
            return redirect(reverse('main'))
        else:
            return render(request, 'register.html', {
                'errors': [
                    'Password and repeated password do not coincide'
                ]
            })
