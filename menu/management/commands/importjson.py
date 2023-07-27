import requests
from django.core.management.base import BaseCommand
from menu.models import MenuItem

class Command(BaseCommand):
    help = 'Import JSON data into the MenuItem table'

    def handle(self, *args, **kwargs):
        url = 'https://www.jsonkeeper.com/b/MDXW'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for item in data:
                MenuItem.objects.create(
                    id=item['id'],
                    title=item['title'],
                    description=item['description'],
                    price=item['price'],
                    spicy_level=item['spicy_level'],
                    category_id=item['category'],  # Assuming 'category' in JSON refers to the Category primary key.
                    cuisine_id=item['cuisine'],  
                )
            self.stdout.write(self.style.SUCCESS('Successfully imported JSON data into the table.'))
        else:
            self.stderr.write(self.style.ERROR(f'Failed to fetch JSON data from URL. Status code: {response.status_code}'))