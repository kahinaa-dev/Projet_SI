from django.db import models

# Create your models here.
class client(models.Model):
    name=models.CharField(max_length=50)
    firstname=models.CharField(max_length=50)
    telephone=models.CharField(max_length=15)
    solde = models.IntegerField()
    historique = models.DateTimeField(auto_now_add=  True)

class user(models.Model):
    ROLE_CHOICES = [
        ('agent', 'Agent'),
        ('responsable', 'Responsable'),
        ('administrator', 'Administrator'),
    ]
    nameuser = models.CharField(max_length=50)
    fnameuser = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20 , choices=ROLE_CHOICES)

class destination(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    geo_zone = models.CharField(max_length=50)
    basic_price = models.FloatField()

class service_type(models.Model):
    SERVICE_CHOICES = [
        ('standard', 'Standard'),
        ('express', 'Express'),
        ('international', 'International'),
    ]

    sname = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        unique=True
    )
    delivery = models.DateField()
    description = models.TextField()

class Pricing(models.Model):
    destination = models.ForeignKey(destination, on_delete=models.CASCADE)
    service_type = models.ForeignKey(service_type, on_delete=models.CASCADE)
    pricing_weight = models.FloatField()
    pricing_volume = models.FloatField()
    calcul_auto_price = models.FloatField()

    class Meta:
        unique_together = ('destination', 'service_type')  




class Pricing(models.Model):
    destination= models.ForeignKey(destination, on_delete=models.CASCADE)
    service_type = models.ForeignKey(service_type, on_delete=models.CASCADE)
    pricing_weight = models.FloatField()
    pricing_volume = models.FloatField()
    calcul_auto_price = models.FloatField()



class expedition(models.Model):
    status_choices=[
        ('created','Created'),
        ('in transaction','In transaction'),
        ('in delivery','In delivery'),
        ('delivered','Delivered'),
        ('in delay','In delay'),
        ('error','Error')
    ]


    id_client=models.ForeignKey(client,on_delete=models.CASCADE)
    id_destination=models.ForeignKey(destination,on_delete=models.CASCADE)
    names = models.ForeignKey(service_type,to_field='sname',on_delete=models.CASCADE)
    weight = models.FloatField()
    volume = models.FloatField()
    total_price=models.FloatField()
    status = models.CharField(max_length=20,choices=status_choices)
    creation_date = models.DateTimeField(auto_now=True)
    description = models.TextField()

class invoice(models.Model):
    id_client=models.ForeignKey(client,on_delete=models.CASCADE)
    date_invoice =models.DateTimeField()
    price_HT = models.FloatField()
    price_tva = models.FloatField()
    price_ttc=models.FloatField()

class payment(models.Model):
    id_invoice=models.ForeignKey(invoice,on_delete=models.CASCADE)
    date = models.DateTimeField()
    price = models.FloatField()
    payment_mode = models.CharField(max_length=50)

class reclamation(models.Model):
    rec_nbr = models.IntegerField()
    unique_nbr = models.ForeignKey(expedition,on_delete=models.CASCADE)
    type = models.CharField(max_length=50,choices=[('expedition','Expedition'),('invoice','Invoice'), ('service','Service')])
    description = models.TextField()
    status = models.CharField(max_length=50)

class suite_reclamation(models.Model):
    id_reclamation = models.ForeignKey(reclamation,on_delete=models.CASCADE)
    action_date = models.DateTimeField()
    comment = models.TextField()
    status_after_action = models.CharField(max_length=50)

class driver(models.Model):
    dname=models.CharField(max_length=50)
    dfname=models.CharField(max_length=50)
    liscence_nbr=models.CharField(max_length=50)
    disponibility=models.CharField(max_length=50)

class vehicule(models.Model):
    immatriculation = models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    consommation = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class tournee(models.Model):
    tournee_date=models.DateTimeField()
    id_driver = models.ForeignKey(driver,on_delete=models.CASCADE)
    id_vehicule = models.ForeignKey(vehicule,on_delete=models.CASCADE)
    duration=models.DurationField()
    consomation=models.CharField(max_length=50)
    distance = models.FloatField()

class accident(models.Model):
    acc_type = models.CharField(max_length=50)
    description = models.TextField()
    date_accident = models.DateTimeField()
    id_tournee=models.ForeignKey(tournee,on_delete=models.CASCADE)
