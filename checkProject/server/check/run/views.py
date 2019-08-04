from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Activity
# Create your views here.


def index(request):
    return HttpResponse("Hello, YOU ARE in the run index.")

def requestQrcode(request):
    return HttpResponse("test")

def verifyQrcode(request):
    seq = "123"
    activities = Activity.objects.filter(seq__exact=seq)
    
    if activities.len()<1:
        return HttpResponse("verify format is wrong")
    print("the activity is " , activity)

    #change the state to end
    activity.state = "end"
    activity.save()
    return HttpResponse("verify")


