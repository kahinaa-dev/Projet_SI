from django import forms
from .models import Client, Chauffeur, Vehicule, Destination, TypeService, Tarification

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address', 'balance', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ChauffeurForm(forms.ModelForm):
    class Meta:
        model = Chauffeur
        fields = ['name', 'email', 'phone', 'permit_number', 'address', 'hire_date', 'is_available', 'salary']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'permit_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['immatriculation', 'type', 'marque', 'capacite', 'consommation', 'etat', 'date_achat', 'dernier_entretien']
        widgets = {
            'immatriculation': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
            'capacite': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'consommation': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'etat': forms.Select(attrs={'class': 'form-select'}),
            'date_achat': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dernier_entretien': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['ville', 'pays', 'zone_geographique', 'tarif_base', 'distance_km', 'temps_estime']
        widgets = {
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'pays': forms.TextInput(attrs={'class': 'form-control'}),
            'zone_geographique': forms.TextInput(attrs={'class': 'form-control'}),
            'tarif_base': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'distance_km': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'temps_estime': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }

class TypeServiceForm(forms.ModelForm):
    class Meta:
        model = TypeService
        fields = ['nom', 'description', 'multiplicateur_tarif', 'temps_livraison_base', 'poids_max', 'est_disponible']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'multiplicateur_tarif': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'temps_livraison_base': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'poids_max': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'est_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TarificationForm(forms.ModelForm):
    class Meta:
        model = Tarification
        fields = ['service', 'destination', 'tarif_par_kg', 'tarif_fixe', 'tarif_minimum']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-select'}),
            'destination': forms.Select(attrs={'class': 'form-select'}),
            'tarif_par_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tarif_fixe': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tarif_minimum': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
