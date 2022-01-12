from django.core.management.base import BaseCommand
from ...models import Country
import csv


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('countries.csv') as csv_file:
            csv_reader=csv.reader(csv_file)
            for country in csv_reader:
                countrywithcode=Country.objects.create(counter=country[0],code=country[1], name=country[2])
        print('Done')