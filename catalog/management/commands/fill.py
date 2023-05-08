from django.core.management import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'auto', 'description': 'vehicle'},
            {'name': 'food', 'description': 'essen'}
        ]

        category_objects = []
        for category_item in category_list:
            category_objects.append(
                Category(**category_item))

        Category.objects.bulk_create(category_objects)

        product_list = [
            {'name': 'potato', 'description': 'vegetable', 'category': 'food', 'purchase_price': 50, 'date_of_creation': '2023-05-01', 'last_modified_date': '2023-05-03'},
            {'name': 'strawberry', 'description': 'berry', 'category': 'food', 'purchase_price': 100, 'date_of_creation': '2023-05-01', 'last_modified_date': '2023-05-03'}
        ]

        product_objects = []
        for product_item in product_list:
            product_objects.append(
                Product(**product_item))

        Product.objects.bulk_create(product_objects)