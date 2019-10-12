"""cvolve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cvolve.main import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('example/', login_required(views.ExampleView.as_view()), name='example'),
    path('offers/', login_required(views.OffersView.as_view()), name='offers'),
    path('accounts/login', views.LoginView.as_view(), name='login'),
    path('signup/', views.RegisterView.as_view(), name="signup"),
    path('to_pdf/', views.PdfView.as_view(), name='to_pdf')
]
