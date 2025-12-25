from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tables/', views.tables, name='tables'),
    path('shipments/', views.shipments, name='shipments'),
    path('billing/', views.billing, name='billing'),
    path('incidents/', views.incidents, name='incidents'),
    path('complaints/', views.complaints, name='complaints'),
    path('tours/', views.tours, name='tours'),
    path('analytics/', views.analytics, name='analytics'),
    
    # Table management URLs
    path('tables/clients/', views.manage_clients, name='manage_clients'),
    path('tables/chauffeurs/', views.manage_chauffeurs, name='manage_chauffeurs'),
    path('tables/vehicules/', views.manage_vehicules, name='manage_vehicules'),
    path('tables/destinations/', views.manage_destinations, name='manage_destinations'),
    path('tables/services/', views.manage_services, name='manage_services'),
    path('tables/tarifications/', views.manage_tarifications, name='manage_tarifications'),
    
    # Delete URLs
    path('tables/client/delete/<int:pk>/', views.delete_client, name='delete_client'),
    path('tables/chauffeur/delete/<int:pk>/', views.delete_chauffeur, name='delete_chauffeur'),
    path('tables/vehicule/delete/<int:pk>/', views.delete_vehicule, name='delete_vehicule'),
    path('tables/destination/delete/<int:pk>/', views.delete_destination, name='delete_destination'),
    path('tables/service/delete/<int:pk>/', views.delete_service, name='delete_service'),
    path('tables/tarification/delete/<int:pk>/', views.delete_tarification, name='delete_tarification'),
]
