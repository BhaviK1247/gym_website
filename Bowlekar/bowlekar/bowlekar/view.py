from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'bow_home.html')

def services(request):
    return render(request,'bow_services.html')

def about(request):
    return render(request,'bow_about.html')
def contact(request):
    return render(request,'bow_contact.html')

def join(request):
    return render(request,'join_now.html')