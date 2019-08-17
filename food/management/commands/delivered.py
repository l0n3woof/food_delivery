from django.core.management.base import BaseCommand
from food.models import Menu, Customer, Deliver
import sys

class Command(BaseCommand):
    help = 'Mark order as delivered'
    def add_arguments(self, parser):
        parser.add_argument('-i', '--id', type=str, help='Mark an order as delivered and delete the same from orders')

    def handle(self, *args, **kwargs):
        order_id = kwargs['id']
        if not order_id:
            print ("Atleast you do it right you are the owner")
            sys.exit()
        else:
            de = Deliver.objects.filter(id=order_id)
            if de:
                order_status = Customer.objects.get(id=order_id)
                order_status.status = "Delivered"
                order_status.save()
                de.delete()
            else:
                print ("Not correct id")
                sys.exit()




