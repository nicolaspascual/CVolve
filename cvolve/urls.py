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
from cvolve.main import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('example/', login_required(views.ExampleView.as_view()), name='example'),

    path('accounts/login', views.LoginView.as_view(), name='login'),
    path('signup/', views.RegisterView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('offers/', login_required(views.OffersView.as_view()), name='offers'),
    path(r'offers/<int:id>/',
         login_required(views.OfferDetailView.as_view()), name='offer_details'),

    path('offers/<int:offer_id>/preview_cv/',
        login_required(views.CVPreviewView.as_view()), name='preview_cv'),

    path('offers/<int:offer_id>/download_cv/',
         login_required(views.CVDownloadView.as_view()), name='download_cv'),
]
