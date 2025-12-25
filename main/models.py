from django.db import models

class Shipment(models.Model):
    name = models.CharField(max_length=100)
    shipment_number = models.CharField(max_length=50, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.FloatField()
    service = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    estimated_delivery = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.shipment_number}"

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Chauffeur(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    permit_number = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    hire_date = models.DateField()
    is_available = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.permit_number}"

class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=50)
    marque = models.CharField(max_length=50)
    capacite = models.FloatField(help_text="Capacité en kg")
    consommation = models.FloatField(help_text="Consommation en L/100km")
    etat = models.CharField(max_length=20, choices=[
        ('Disponible', 'Disponible'),
        ('En service', 'En service'),
        ('Maintenance', 'Maintenance'),
        ('Hors service', 'Hors service'),
    ])
    date_achat = models.DateField()
    dernier_entretien = models.DateField()

    def __str__(self):
        return f"{self.immatriculation} - {self.type}"

class Destination(models.Model):
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    zone_geographique = models.CharField(max_length=50)
    tarif_base = models.DecimalField(max_digits=8, decimal_places=2)
    distance_km = models.FloatField(help_text="Distance depuis le dépôt principal")
    temps_estime = models.FloatField(help_text="Temps estimé en heures")

    def __str__(self):
        return f"{self.ville}, {self.pays}"

class TypeService(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    multiplicateur_tarif = models.FloatField(default=1.0)
    temps_livraison_base = models.FloatField(help_text="Temps de livraison de base en heures")
    poids_max = models.FloatField(help_text="Poids maximum autorisé en kg")
    est_disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Tarification(models.Model):
    service = models.ForeignKey(TypeService, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    tarif_par_kg = models.DecimalField(max_digits=8, decimal_places=2)
    tarif_fixe = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    tarif_minimum = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['service', 'destination']

    def __str__(self):
        return f"{self.service.nom} - {self.destination.ville}: {self.tarif_par_kg}/kg"
