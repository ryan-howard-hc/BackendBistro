# menu/management/commands/menujson.py
import json
import os
from django.core.management.base import BaseCommand
from menu.models import MenuItem

class Command(BaseCommand):
    help = 'Import JSON data into the MenuItem table'

    def handle(self, *args, **kwargs):
        json_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'menu.json')
        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                MenuItem.objects.create(
                    title=item['title'],
                    description=item['description'],
                    price=item['price'],
                    spicy_level=item['spicy_level'],
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported JSON data into the table.'))

