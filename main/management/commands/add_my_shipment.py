from django.core.management.base import BaseCommand
from main.models import Shipment
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Add a test shipment with user name'

    def handle(self, *args, **options):
        # Create a test shipment - replace "Your Name" with your actual name
        shipment = Shipment.objects.create(
            name='Amira',  # Changed to your name
            shipment_number='TEST001',
            origin='Current Location',
            destination='Target Destination',
            weight=2.5,
            service='Express',
            status='In Transit',
            estimated_delivery=date.today() + timedelta(days=3)
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created shipment: {shipment.shipment_number} for {shipment.name}'))
        self.stdout.write(self.style.SUCCESS('Visit http://127.0.0.1:8000/shipments/ to see it!'))
