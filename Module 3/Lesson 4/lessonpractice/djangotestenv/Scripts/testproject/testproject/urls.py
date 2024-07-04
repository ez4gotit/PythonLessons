"""
URL configuration for testproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import testapp
from django.urls import path , include
from django.shortcuts import redirect
from django.views.generic import RedirectView
urlpatterns = [

    #http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='admin/', permanent=True)),

    path('testapp/', include('testapp.urls'))
]
