"""
URL configuration for proyect_rest_civa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from api.views import *

urlpatterns = [
    path('s1_cotizacion/', s1_cotizacion, name='s1_cotizacion'),
    path('s2_emisor/', s2_emisor, name='s2_emisor'),
    path('s3_encomienda/', s3_encomienda, name='s3_encomienda'),
    path('s5_destinatario/', s5_destinatario, name='s5_destinatario'),
    path('s6_registro_encomienda/', s6_registro_encomienda, name='s6_registro_encomienda'),

]