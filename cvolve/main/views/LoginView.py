from django.contrib import auth
from django.views import View
from django.shortcuts import render, redirect, reverse


class LoginView(View):
    
    def get(self, request):
        # <view logic>
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # authentication of the user, to check if it's active or None
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            # this is where the user login actually happens, before this the user
            # is not logged in.
            auth.login(request, user)
            return redirect(reverse('main'))

        else:
            return render(request, 'registration/login.html', {
                'errors': ['The user does not exist or the password is incorrect']
            })