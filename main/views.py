from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def tables(request):
    return render(request, 'tables.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Shipment, Client, Chauffeur, Vehicule, Destination, TypeService, Tarification
from .forms import ShipmentForm
from .table_forms import ClientForm, ChauffeurForm, VehiculeForm, DestinationForm, TypeServiceForm, TarificationForm
import uuid
from datetime import date

def tables(request):
    context = {
        'clients': Client.objects.all().order_by('name'),
        'chauffeurs': Chauffeur.objects.all().order_by('name'),
        'vehicules': Vehicule.objects.all().order_by('immatriculation'),
        'destinations': Destination.objects.all().order_by('ville'),
        'services': TypeService.objects.all().order_by('nom'),
        'tarifications': Tarification.objects.all().order_by('service', 'destination'),
    }
    return render(request, 'tables.html', context)

def manage_clients(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client created successfully!')
            return redirect('manage_clients')
    else:
        form = ClientForm()
    
    return render(request, 'tables/clients_manage.html', {'form': form, 'clients': Client.objects.all().order_by('name')})

def manage_chauffeurs(request):
    if request.method == 'POST':
        form = ChauffeurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Chauffeur created successfully!')
            return redirect('tables')
    else:
        form = ChauffeurForm()
    
    return render(request, 'tables/chauffeurs.html', {'form': form, 'chauffeurs': Chauffeur.objects.all().order_by('name')})

def manage_vehicules(request):
    if request.method == 'POST':
        form = VehiculeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Véhicule created successfully!')
            return redirect('tables')
    else:
        form = VehiculeForm()
    
    return render(request, 'tables/vehicules.html', {'form': form, 'vehicules': Vehicule.objects.all().order_by('immatriculation')})

def manage_destinations(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination created successfully!')
            return redirect('tables')
    else:
        form = DestinationForm()
    
    return render(request, 'tables/destinations.html', {'form': form, 'destinations': Destination.objects.all().order_by('ville')})

def manage_services(request):
    if request.method == 'POST':
        form = TypeServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service type created successfully!')
            return redirect('tables')
    else:
        form = TypeServiceForm()
    
    return render(request, 'tables/services.html', {'form': form, 'services': TypeService.objects.all().order_by('nom')})

def manage_tarifications(request):
    if request.method == 'POST':
        form = TarificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarification created successfully!')
            return redirect('tables')
    else:
        form = TarificationForm()
    
    return render(request, 'tables/tarifications.html', {'form': form, 'tarifications': Tarification.objects.all().order_by('service', 'destination')})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, 'Client deleted successfully!')
    return redirect('manage_clients')

def delete_chauffeur(request, pk):
    chauffeur = get_object_or_404(Chauffeur, pk=pk)
    chauffeur.delete()
    messages.success(request, 'Chauffeur deleted successfully!')
    return redirect('tables')

def delete_vehicule(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    vehicule.delete()
    messages.success(request, 'Véhicule deleted successfully!')
    return redirect('tables')

def delete_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    destination.delete()
    messages.success(request, 'Destination deleted successfully!')
    return redirect('tables')

def delete_service(request, pk):
    service = get_object_or_404(TypeService, pk=pk)
    service.delete()
    messages.success(request, 'Service type deleted successfully!')
    return redirect('tables')

def delete_tarification(request, pk):
    tarification = get_object_or_404(Tarification, pk=pk)
    tarification.delete()
    messages.success(request, 'Tarification deleted successfully!')
    return redirect('tables')

def shipments(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        print(f"Form submitted: {request.POST}")
        print(f"Form is valid: {form.is_valid()}")
        if form.is_valid():
            shipment = form.save(commit=False)
            # Generate unique shipment number
            shipment.shipment_number = f"TRK{uuid.uuid4().hex[:6].upper()}"
            shipment.status = 'Pending'
            shipment.save()
            print(f"Shipment saved: {shipment.shipment_number}")
            messages.success(request, f'Shipment {shipment.shipment_number} created successfully!')
            return redirect('shipments')
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = ShipmentForm()
    
    all_shipments = Shipment.objects.all().order_by('-estimated_delivery')
    print(f"Total shipments in database: {all_shipments.count()}")
    return render(request, 'shipments.html', {'shipments': all_shipments, 'form': form})


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
