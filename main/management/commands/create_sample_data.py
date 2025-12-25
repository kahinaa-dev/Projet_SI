from django.core.management.base import BaseCommand
from main.models import Shipment
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Create sample shipment data'

    def handle(self, *args, **options):
        # Clear existing shipments
        Shipment.objects.all().delete()
        
        # Sample shipments
        shipments_data = [
            {
                'name': 'John Doe',
                'shipment_number': 'TRK001',
                'origin': 'New York',
                'destination': 'Boston',
                'weight': 5.2,
                'service': 'Express',
                'status': 'In Transit',
                'estimated_delivery': date.today() + timedelta(days=2)
            },
            {
                'name': 'Jane Smith',
                'shipment_number': 'TRK002',
                'origin': 'Los Angeles',
                'destination': 'San Francisco',
                'weight': 2.8,
                'service': 'Standard',
                'status': 'Delivered',
                'estimated_delivery': date.today() - timedelta(days=1)
            },
            {
                'name': 'Bob Johnson',
                'shipment_number': 'TRK003',
                'origin': 'Chicago',
                'destination': 'Detroit',
                'weight': 8.5,
                'service': 'Standard',
                'status': 'Pending',
                'estimated_delivery': date.today() + timedelta(days=3)
            },
            {
                'name': 'Alice Cooper',
                'shipment_number': 'TRK004',
                'origin': 'Miami',
                'destination': 'Atlanta',
                'weight': 3.1,
                'service': 'Express',
                'status': 'Delayed',
                'estimated_delivery': date.today() + timedelta(days=4)
            },
            {
                'name': 'Tom Wilson',
                'shipment_number': 'TRK005',
                'origin': 'Seattle',
                'destination': 'Portland',
                'weight': 1.5,
                'service': 'Standard',
                'status': 'Out for Delivery',
                'estimated_delivery': date.today()
            },
            {
                'name': 'Carol White',
                'shipment_number': 'TRK006',
                'origin': 'Denver',
                'destination': 'Phoenix',
                'weight': 4.7,
                'service': 'International',
                'status': 'Lost',
                'estimated_delivery': date.today() + timedelta(days=5)
            }
        ]
        
        # Create shipments
        for data in shipments_data:
            shipment = Shipment.objects.create(**data)
            self.stdout.write(f'Created shipment: {shipment.shipment_number}')
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(shipments_data)} shipments'))
