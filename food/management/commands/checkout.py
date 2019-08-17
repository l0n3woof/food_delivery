from django.core.management.base import BaseCommand
from food.models import Menu, Customer, Deliver
import sys

class Command(BaseCommand):
    help = 'Customer cart checkout'
    def add_arguments(self, parser):
        parser.add_argument('-i', '--id', type=str, help='Enter id to complete payment')

    def handle(self, *args, **kwargs):
        order_id = kwargs['id']
        if not order_id:
            print ("No money, ring us to get free food.")
            sys.exit()
        payment = Customer.objects.get(id=order_id)
        if payment:
            payment.status = "paid"
            payment.save()
            save_deliver = Deliver.objects.create(id=payment.id, status=payment.status, order=payment.cart)
            save_deliver.save()
        else:
            print ("No matching order")


