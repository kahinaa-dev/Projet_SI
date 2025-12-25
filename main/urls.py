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
]
