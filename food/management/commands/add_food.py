from django.core.management.base import BaseCommand
from food.models import Menu
import sys

class Command(BaseCommand):
    help = 'Create food menu'
    def add_arguments(self, parser):
        parser.add_argument('-f', '--food', type=str, help='Enter the food name')
        parser.add_argument('-d', '--description', type=str, help='Enter food Description')

    def handle(self, *args, **kwargs):
        food = kwargs['food']
        if not food:
            print ("Atleast enter a food name, I'll let the description pass")
            sys.exit()
        description = kwargs['description']
        if not description:
            description = 'Guess yourself'
        Menu.objects.create(food=food, description=description)
        print ("Your Menu has just been updated.")




