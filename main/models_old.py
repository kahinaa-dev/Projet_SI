from django.db import models

class Shipment(models.Model):
    name = models.CharField(max_length=100)
    shipment_number = models.CharField(max_length=50, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.FloatField()
    volume = models.FloatField(default=0.0, help_text="Volume en m³")
    service = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    estimated_delivery = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

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
    tarif_volume = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
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
    tarif_par_volume = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    tarif_fixe = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    tarif_minimum = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['service', 'destination']

    def __str__(self):
        return f"{self.service.nom} - {self.destination.ville}: {self.tarif_par_kg}/kg"

class Tournee(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    kilometrage = models.FloatField(default=0.0)
    duree = models.FloatField(default=0.0, help_text="Durée en heures")
    consommation_carburant = models.FloatField(default=0.0)
    statut = models.CharField(max_length=20, choices=[
        ('Planifiée', 'Planifiée'),
        ('En cours', 'En cours'),
        ('Terminée', 'Terminée'),
        ('Annulée', 'Annulée'),
    ], default='Planifiée')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tournee {self.numero} - {self.chauffeur.name}"

class Facture(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_emission = models.DateField(auto_now_add=True)
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2)
    montant_tva = models.DecimalField(max_digits=10, decimal_places=2)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=[
        ('Non payée', 'Non payée'),
        ('Partiellement payée', 'Partiellement payée'),
        ('Payée', 'Payée'),
        ('Annulée', 'Annulée'),
    ], default='Non payée')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Facture {self.numero} - {self.client.name}"

class Paiement(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()
    mode_paiement = models.CharField(max_length=50, choices=[
        ('Espèces', 'Espèces'),
        ('Carte bancaire', 'Carte bancaire'),
        ('Virement', 'Virement'),
        ('Chèque', 'Chèque'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paiement {self.montant}€ - Facture {self.facture.numero}"

class Incident(models.Model):
    TYPE_INCIDENT_CHOICES = [
        ('Retard', 'Retard'),
        ('Perte', 'Perte'),
        ('Endommagement', 'Endommagement'),
        ('Problème technique', 'Problème technique'),
        ('Accident', 'Accident'),
        ('Autre', 'Autre'),
    ]
    
    type_incident = models.CharField(max_length=50, choices=TYPE_INCIDENT_CHOICES)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True, blank=True)
    tournee = models.ForeignKey(Tournee, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    date_incident = models.DateTimeField(auto_now_add=True)
    gravite = models.CharField(max_length=20, choices=[
        ('Mineure', 'Mineure'),
        ('Moyenne', 'Moyenne'),
        ('Majeure', 'Majeure'),
        ('Critique', 'Critique'),
    ], default='Moyenne')
    resolu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Incident {self.type_incident} - {self.date_incident.date()}"

class Reclamation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True, blank=True)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, null=True, blank=True)
    nature = models.CharField(max_length=100)
    description = models.TextField()
    date_reclamation = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=[
        ('En cours', 'En cours'),
        ('Résolue', 'Résolue'),
        ('Annulée', 'Annulée'),
    ], default='En cours')
    agent_responsable = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réclamation {self.nature} - {self.client.name}"

class ShipmentTracking(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    etat = models.CharField(max_length=50, choices=[
        ('Créé', 'Créé'),
        ('En transit', 'En transit'),
        ('En centre de tri', 'En centre de tri'),
        ('En cours de livraison', 'En cours de livraison'),
        ('Livré', 'Livré'),
        ('Échec de livraison', 'Échec de livraison'),
    ])
    lieu = models.CharField(max_length=100)
    date_etape = models.DateTimeField(auto_now_add=True)
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.SET_NULL, null=True, blank=True)
    commentaires = models.TextField(blank=True)

    def __str__(self):
        return f"Tracking {self.shipment.shipment_number} - {self.etat}"
