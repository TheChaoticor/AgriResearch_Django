from django.shortcuts import render
from django.conf import settings


# Create your views here.
def all_research(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
   
    return render(request,'research/all_research.html',context)


# In your views.py

