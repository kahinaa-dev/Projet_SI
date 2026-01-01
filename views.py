from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import *


# EXPEDITION CREATION + PRICE CALC

def create_expedition(request):
    client_id = request.POST['client_id']
    destination_id = request.POST['destination_id']
    service_name = request.POST['service_name']
    weight = float(request.POST['weight'])
    volume = float(request.POST['volume'])

    client_obj = get_object_or_404(client, id=client_id)
    destination_obj = get_object_or_404(destination, id=destination_id)
    service_obj = get_object_or_404(service_type, sname=service_name)

    pricing = get_object_or_404(
        Pricing,
        destination=destination_obj,
        service_type=service_obj
    )

    total_price = (
        pricing.pricing_weight * weight +
        pricing.pricing_volume * volume
    )

    exp = expedition.objects.create(
        id_client=client_obj,
        id_destination=destination_obj,
        names=service_obj,
        weight=weight,
        volume=volume,
        total_price=total_price,
        status='created',
        description=''
    )

    return JsonResponse({"expedition_id": exp.id, "total_price": total_price})



# INVOICE CREATION

def create_invoice(request, client_id):
    client_obj = get_object_or_404(client, id=client_id)
    expeditions = expedition.objects.filter(id_client=client_obj)

    price_ht = sum(e.total_price for e in expeditions)
    price_tva = price_ht * 0.19
    price_ttc = price_ht + price_tva

    invoice_obj = invoice.objects.create(
        id_client=client_obj,
        date_invoice=timezone.now(),
        price_HT=price_ht,
        price_tva=price_tva,
        price_ttc=price_ttc
    )

    return JsonResponse({
        "invoice_id": invoice_obj.id,
        "HT": price_ht,
        "TVA": price_tva,
        "TTC": price_ttc
    })



# PAYMENT + CLIENT BALANCE UPDATE

def make_payment(request):
    invoice_id = request.POST['invoice_id']
    amount = float(request.POST['amount'])
    mode = request.POST['mode']

    invoice_obj = get_object_or_404(invoice, id=invoice_id)
    client_obj = invoice_obj.id_client

    payment.objects.create(
        id_invoice=invoice_obj,
        date=timezone.now(),
        price=amount,
        payment_mode=mode
    )

    client_obj.solde -= amount
    client_obj.save()

    return JsonResponse({"message": "Payment recorded"})



# RECLAMATION + HISTORY

def create_reclamation(request):
    expedition_id = request.POST['expedition_id']
    rec_type = request.POST['type']
    description = request.POST['description']

    exp = get_object_or_404(expedition, id=expedition_id)

    rec = reclamation.objects.create(
        rec_nbr=timezone.now().timestamp(),
        unique_nbr=exp,
        type=rec_type,
        description=description,
        status='new'
    )

    suite_reclamation.objects.create(
        id_reclamation=rec,
        action_date=timezone.now(),
        comment="Reclamation created",
        status_after_action='new'
    )

    return JsonResponse({"reclamation_id": rec.id})
