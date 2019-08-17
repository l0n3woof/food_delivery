from django.core.management.base import BaseCommand
from food.models import Menu
import sys

class Command(BaseCommand):
    help = 'See food description'
    def add_arguments(self, parser):
        parser.add_argument('-i', '--id', type=int, help='Enter the food serial number')

    def handle(self, *args, **kwargs):
        food_id = kwargs['id']
        if not food_id:
            print ("Next time please remember the food id, now go back to the menu")
            sys.exit()
        desc = Menu.objects.filter(id=food_id).values('food','description')
        for d in desc:
            print (d['food'] +' :- ' +d['description'])




