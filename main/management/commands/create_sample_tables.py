from django.core.management.base import BaseCommand
from main.models import Client, Chauffeur, Vehicule, Destination, TypeService, Tarification
from decimal import Decimal
from datetime import date

class Command(BaseCommand):
    help = 'Create sample data for all database tables'

    def handle(self, *args, **options):
        # Create sample clients
        clients_data = [
            {
                'name': 'Jean Dupont',
                'email': 'jean.dupont@email.com',
                'phone': '0123456789',
                'address': '15 Rue de la Paix, Paris',
                'balance': Decimal('150.50')
            },
            {
                'name': 'Marie Martin',
                'email': 'marie.martin@email.com',
                'phone': '0234567890',
                'address': '25 Avenue des Champs, Lyon',
                'balance': Decimal('75.25')
            },
            {
                'name': 'Pierre Bernard',
                'email': 'pierre.bernard@email.com',
                'phone': '0345678901',
                'address': '8 Boulevard du Soleil, Marseille',
                'balance': Decimal('0.00')
            }
        ]

        for data in clients_data:
            client, created = Client.objects.get_or_create(
                email=data['email'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created client: {client.name}')

        # Create sample chauffeurs
        chauffeurs_data = [
            {
                'name': 'Robert Laurent',
                'email': 'robert.laurent@email.com',
                'phone': '0456789012',
                'permit_number': 'PERM001',
                'address': '10 Rue du Garage, Paris',
                'hire_date': date(2020, 1, 15),
                'salary': Decimal('2500.00')
            },
            {
                'name': 'Michel Robert',
                'email': 'michel.robert@email.com',
                'phone': '0567890123',
                'permit_number': 'PERM002',
                'address': '5 Place du Convoi, Lyon',
                'hire_date': date(2019, 3, 20),
                'salary': Decimal('2400.00')
            }
        ]

        for data in chauffeurs_data:
            chauffeur, created = Chauffeur.objects.get_or_create(
                permit_number=data['permit_number'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created chauffeur: {chauffeur.name}')

        # Create sample véhicules
        vehicules_data = [
            {
                'immatriculation': 'AB-123-CD',
                'type': 'Camionette',
                'marque': 'Renault',
                'capacite': 1500.0,
                'consommation': 8.5,
                'etat': 'Disponible',
                'date_achat': date(2021, 6, 1),
                'dernier_entretien': date(2024, 1, 15)
            },
            {
                'immatriculation': 'EF-456-GH',
                'type': 'Camion',
                'marque': 'Mercedes',
                'capacite': 3500.0,
                'consommation': 12.0,
                'etat': 'En service',
                'date_achat': date(2020, 3, 15),
                'dernier_entretien': date(2024, 2, 1)
            }
        ]

        for data in vehicules_data:
            vehicule, created = Vehicule.objects.get_or_create(
                immatriculation=data['immatriculation'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created véhicule: {vehicule.immatriculation}')

        # Create sample destinations
        destinations_data = [
            {
                'ville': 'Paris',
                'pays': 'France',
                'zone_geographique': 'Île-de-France',
                'tarif_base': Decimal('10.00'),
                'distance_km': 0.0,
                'temps_estime': 0.0
            },
            {
                'ville': 'Lyon',
                'pays': 'France',
                'zone_geographique': 'Auvergne-Rhône-Alpes',
                'tarif_base': Decimal('25.00'),
                'distance_km': 465.0,
                'temps_estime': 4.5
            },
            {
                'ville': 'Marseille',
                'pays': 'France',
                'zone_geographique': 'Provence-Alpes-Côte d\'Azur',
                'tarif_base': Decimal('35.00'),
                'distance_km': 775.0,
                'temps_estime': 7.5
            },
            {
                'ville': 'Bruxelles',
                'pays': 'Belgique',
                'zone_geographique': 'International',
                'tarif_base': Decimal('50.00'),
                'distance_km': 310.0,
                'temps_estime': 3.0
            }
        ]

        for data in destinations_data:
            destination, created = Destination.objects.get_or_create(
                ville=data['ville'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created destination: {destination.ville}')

        # Create sample types de service
        services_data = [
            {
                'nom': 'Standard',
                'description': 'Service standard de livraison',
                'multiplicateur_tarif': 1.0,
                'temps_livraison_base': 48.0,
                'poids_max': 1000.0
            },
            {
                'nom': 'Express',
                'description': 'Livraison express en 24h',
                'multiplicateur_tarif': 1.5,
                'temps_livraison_base': 24.0,
                'poids_max': 500.0
            },
            {
                'nom': 'International',
                'description': 'Service international',
                'multiplicateur_tarif': 2.0,
                'temps_livraison_base': 72.0,
                'poids_max': 2000.0
            }
        ]

        for data in services_data:
            service, created = TypeService.objects.get_or_create(
                nom=data['nom'],
                defaults=data
            )
            if created:
                self.stdout.write(f'Created service type: {service.nom}')

        # Create sample tarifications
        tarifications_data = [
            {'service_nom': 'Standard', 'destination_ville': 'Lyon', 'tarif_par_kg': Decimal('2.50'), 'tarif_fixe': Decimal('15.00')},
            {'service_nom': 'Express', 'destination_ville': 'Lyon', 'tarif_par_kg': Decimal('3.75'), 'tarif_fixe': Decimal('25.00')},
            {'service_nom': 'International', 'destination_ville': 'Bruxelles', 'tarif_par_kg': Decimal('5.00'), 'tarif_fixe': Decimal('40.00')},
        ]

        for data in tarifications_data:
            service = TypeService.objects.get(nom=data['service_nom'])
            destination = Destination.objects.get(ville=data['destination_ville'])
            
            tarification, created = Tarification.objects.get_or_create(
                service=service,
                destination=destination,
                defaults={
                    'tarif_par_kg': data['tarif_par_kg'],
                    'tarif_fixe': data['tarif_fixe'],
                    'tarif_minimum': Decimal('10.00')
                }
            )
            if created:
                self.stdout.write(f'Created tarification: {tarification}')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
