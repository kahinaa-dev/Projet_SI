from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def tables(request):
    return render(request, 'tables.html')

from django.shortcuts import render
from .models import Shipment

def shipments(request):
    all_shipments = Shipment.objects.all()
    return render(request, 'shipments.html', {'shipments': all_shipments})


def billing(request):
    return render(request, 'billing.html')

def incidents(request):
    return render(request, 'incidents.html')

def complaints(request):
    return render(request, 'complaints.html')

def tours(request):
    return render(request, 'tours.html')

def analytics(request):
    return render(request, 'analytics.html')
