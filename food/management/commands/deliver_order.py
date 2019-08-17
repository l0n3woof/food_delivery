from django.core.management.base import BaseCommand
from food.models import Menu, Customer, Deliver
import sys

class Command(BaseCommand):
    help = 'Check current orders'

    def handle(self, *args, **kwargs):
        orders = Deliver.objects.all()
        for order in orders:
            print (str(order.id) + '. ' + order.order)
