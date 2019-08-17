from django.core.management.base import BaseCommand
from food.models import Menu
import sys

class Command(BaseCommand):
    help = 'Delete from food menu'
    def add_arguments(self, parser):
        parser.add_argument('-i', '--id', type=int, help='Enter the food id to delete')

    def handle(self, *args, **kwargs):
        food_id = kwargs['id']
        if not food_id:
            print ("You really want to delete something?")
            sys.exit()
        Menu.objects.filter(id=food_id).delete()
        print ("Your Menu has just been updated.")




