from django.core.management.base import BaseCommand
from food.models import Menu, Customer, Deliver
import sys

class Command(BaseCommand):
    help = 'View customer order'
    def add_arguments(self, parser):
        parser.add_argument('-i', '--id', type=str, help='Enter order id to check your order status')

    def handle(self, *args, **kwargs):
        order_id = kwargs['id']
        if not order_id:
            print ("Did you even order something?")
            sys.exit()
        try:
            order = Customer.objects.filter(id=int(order_id)).values('cart', 'status')[0]
            print (order['cart'] + ' and status is ' + order['status'])
        except IndexError:
            print ("Please order correct order id.")
