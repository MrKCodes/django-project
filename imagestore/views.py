from django.shortcuts import render
from django.http import HttpResponse
from imagestore.forms import TrackerForm
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def tracker(request):
    track = TrackerForm()
    return render(request, 'tracker.html', {'form':track})

def output(request):
    output_data = TrackerForm(request)
    out = output_data.save(commit=True)
    return render(request,'output.html', {'details':out})