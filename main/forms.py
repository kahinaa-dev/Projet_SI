from django import forms
from .models import Shipment

SERVICE_CHOICES = [
    ('Standard', 'Standard'),
    ('Express', 'Express'),
    ('International', 'International'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('In Transit', 'In Transit'),
    ('Delivered', 'Delivered'),
    ('Delayed', 'Delayed'),
    ('Out for Delivery', 'Out for Delivery'),
    ('Lost', 'Lost'),
]

class ShipmentForm(forms.ModelForm):
    service = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Shipment
        fields = ['name', 'origin', 'destination', 'weight', 'service', 'estimated_delivery']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter origin city'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter destination city'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Weight in kg'}),
            'estimated_delivery': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
