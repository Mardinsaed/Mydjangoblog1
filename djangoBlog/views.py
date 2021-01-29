from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hi mardin')
    return render(request , 'about.html')

def home(request):
    # return HttpResponse('HOME')
        return render(request , 'hom.html')
