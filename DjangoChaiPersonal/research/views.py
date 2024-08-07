from django.shortcuts import render

# Create your views here.
def all_research(request):
   
    return render(request,'research/all_research.html')


