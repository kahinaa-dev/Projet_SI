from django.contrib import admin
from .models import Shipment, Client, Chauffeur, Vehicule, Destination, TypeService, Tarification

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('shipment_number', 'name', 'origin', 'destination', 'status', 'estimated_delivery')
    list_filter = ('status', 'service', 'origin', 'destination')
    search_fields = ('name', 'shipment_number', 'origin', 'destination')
    ordering = ('-estimated_delivery',)
    readonly_fields = ('shipment_number',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'balance', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('name',)
    readonly_fields = ('created_at',)

@admin.register(Chauffeur)
class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'permit_number', 'is_available', 'hire_date', 'salary')
    list_filter = ('is_available', 'hire_date')
    search_fields = ('name', 'email', 'permit_number')
    ordering = ('name',)

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'type', 'marque', 'capacite', 'etat', 'date_achat')
    list_filter = ('etat', 'type', 'marque')
    search_fields = ('immatriculation', 'type', 'marque')
    ordering = ('immatriculation',)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('ville', 'pays', 'zone_geographique', 'tarif_base', 'distance_km')
    list_filter = ('zone_geographique', 'pays')
    search_fields = ('ville', 'pays')
    ordering = ('ville',)

@admin.register(TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'multiplicateur_tarif', 'temps_livraison_base', 'poids_max', 'est_disponible')
    list_filter = ('est_disponible',)
    search_fields = ('nom', 'description')
    ordering = ('nom',)

@admin.register(Tarification)
class TarificationAdmin(admin.ModelAdmin):
    list_display = ('service', 'destination', 'tarif_par_kg', 'tarif_fixe', 'tarif_minimum', 'date_mise_a_jour')
    list_filter = ('service', 'destination')
    search_fields = ('service__nom', 'destination__ville')
    ordering = ('service', 'destination')
