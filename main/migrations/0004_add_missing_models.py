# Generated manually for new models

from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_chauffeur_client_destination_typeservice_vehicule_and_more'),
    ]

    operations = [
        # Add new fields to existing models
        migrations.AddField(
            model_name='destination',
            name='tarif_volume',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=8),
        ),
        migrations.AddField(
            model_name='shipment',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.client'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='prix_total',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=10),
        ),
        migrations.AddField(
            model_name='shipment',
            name='volume',
            field=models.FloatField(default=0.0, help_text='Volume en m³'),
        ),
        migrations.AddField(
            model_name='tarification',
            name='tarif_par_volume',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=8),
        ),
        
        # Create new models
        migrations.CreateModel(
            name='Tournee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50, unique=True)),
                ('date', models.DateField()),
                ('kilometrage', models.FloatField(default=0.0)),
                ('duree', models.FloatField(default=0.0, help_text='Durée en heures')),
                ('consommation_carburant', models.FloatField(default=0.0)),
                ('statut', models.CharField(choices=[('Planifiée', 'Planifiée'), ('En cours', 'En cours'), ('Terminée', 'Terminée'), ('Annulée', 'Annulée')], default='Planifiée', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chauffeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chauffeur')),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50, unique=True)),
                ('date_emission', models.DateField(auto_now_add=True)),
                ('montant_ht', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montant_tva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montant_ttc', models.DecimalField(decimal_places=2, max_digits=10)),
                ('statut', models.CharField(choices=[('Non payée', 'Non payée'), ('Partiellement payée', 'Partiellement payée'), ('Payée', 'Payée'), ('Annulée', 'Annulée')], default='Non payée', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateField()),
                ('mode_paiement', models.CharField(choices=[('Espèces', 'Espèces'), ('Carte bancaire', 'Carte bancaire'), ('Virement', 'Virement'), ('Chèque', 'Chèque')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.facture')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_incident', models.CharField(choices=[('Retard', 'Retard'), ('Perte', 'Perte'), ('Endommagement', 'Endommagement'), ('Problème technique', 'Problème technique'), ('Accident', 'Accident'), ('Autre', 'Autre')], max_length=50)),
                ('description', models.TextField()),
                ('date_incident', models.DateTimeField(auto_now_add=True)),
                ('gravite', models.CharField(choices=[('Mineure', 'Mineure'), ('Moyenne', 'Moyenne'), ('Majeure', 'Majeure'), ('Critique', 'Critique')], default='Moyenne', max_length=20)),
                ('resolu', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.shipment')),
                ('tournee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tournee')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_reclamation', models.DateField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('En cours', 'En cours'), ('Résolue', 'Résolue'), ('Annulée', 'Annulée')], default='En cours', max_length=20)),
                ('agent_responsable', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
                ('facture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.facture')),
                ('shipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(choices=[('Créé', 'Créé'), ('En transit', 'En transit'), ('En centre de tri', 'En centre de tri'), ('En cours de livraison', 'En cours de livraison'), ('Livré', 'Livré'), ('Échec de livraison', 'Échec de livraison')], max_length=50)),
                ('lieu', models.CharField(max_length=100)),
                ('date_etape', models.DateTimeField(auto_now_add=True)),
                ('commentaires', models.TextField(blank=True)),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.chauffeur')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shipment')),
            ],
        ),
    ]
