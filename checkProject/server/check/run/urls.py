from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('verifyQrcode' , views.verifyQrcode, name = 'verify'),
    path('requestQrcode' , views.requestQrcode, name = 'request'),
]
