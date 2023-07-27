# menu/management/commands/menujson.py
import json
import os
from django.core.management.base import BaseCommand
from menu.models import MenuItem

class Command(BaseCommand):
    help = 'Import JSON data into the MenuItem table'

    def handle(self, *args, **kwargs):
        print(f"Current working directory: {os.getcwd()}")
        json_file = 'menu.json'
        json_file_path = os.path.abspath(json_file)
        print(f"JSON file path: {json_file_path}")
        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data["menuItems"]:
                MenuItem.objects.create(
                    id=item['id'],
                    title=item['name'],
                    description=item['description'],
                    price=float(item['price'].replace('$', '')),
                    spicy_level=item['spicy_level'],
        )
        self.stdout.write(self.style.SUCCESS('Successfully imported JSON data into the table.'))

