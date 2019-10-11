from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class RegisterView(View):
    
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.POST.get('password') == request.POST.get('repeat_password'):
            try:
                user = User.objects.create_user(
                    request.POST.get('username'),
                    password=request.POST.get('password')
                )
                user.save()
                login(request, user)
                return redirect(reverse('main'))
            except IntegrityError:
                return render(request, 'register.html', {
                    'errors': ['The user does already exist or the username is invalid']
                })
        else:
            return render(request, 'register.html', {
                'errors': ['Password and repeated password do not coincide']
            })
