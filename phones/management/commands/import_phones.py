import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(
                id=int(phone['id']),
                name=phone['name'],
                image=phone['image'],
                price=int(phone['price']),
                release_date=phone['release_date'],
                lte_exists=bool(phone['lte_exists'])
            )
