from django.core.management.base import BaseCommand
from food.models import Menu
import sys

class Command(BaseCommand):
    help = 'See food menu'

    def handle(self, *args, **kwargs):
        all_food = Menu.objects.all()
        for food in all_food:
            string = str(food.id) + '. ' + food.food
            print (string)
        print ("You can easily order the food using the serial number")




