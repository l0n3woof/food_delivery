from django.core.management.base import BaseCommand
from food.models import Menu, Customer, Deliver
import sys

class Command(BaseCommand):
    help = 'Customer cart for order'
    def add_arguments(self, parser):
        parser.add_argument('-o', '--order', type=str, help='Enter the food serial number for order,\
                you can enter multiple numbers seprated by comma eg. "1,4,5"')

    def handle(self, *args, **kwargs):
        order_numbers = kwargs['order']
        if not order_numbers:
            print ("Are you just passing time here")
            sys.exit()
        if not ',' in order_numbers:
            o_string = 'Order is '
            try:
                o_string += Menu.objects.filter(id=int(order_numbers)).values_list('food', flat=True)[0]
                status = "Proccessing"
                cart = o_string
                save_order = Customer.objects.create(status=status, cart=cart)
                save_order.save()
                print ("Remember your order id to check the stauts. Your order id is " + str(save_order.id) + " .Hush now do the payment.")
            except IndexError:
                print ("The item you chose is not in the menu.")
        else:
            order = order_numbers.split(',')
            o_string = 'Order is '
            for o in order:
                try:
                    o_string = o_string + Menu.objects.filter(id=int(o)).values_list('food', flat=True)[0] + ' '
                except IndexError:
                    print ("Your order number " + o + " can't be processed it either not in menu or is finished.")
            if not o_string=='Order is ':
                status = "Proccessing"
                save_order = Customer.objects.create(status=status, cart=o_string)
                save_order.save()
                print ("Remember your order id to check the stauts. Your order id is " + str(save_order.id) + " .Hush now do the payment.")
            else:
                print ("Man how can you miss all of them. Are you nervous?")




