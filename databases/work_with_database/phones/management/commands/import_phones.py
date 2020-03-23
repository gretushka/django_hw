import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                if Phone.objects.filter(id=line[0]):
                    pass
                else:
                    Phone.objects.create(id = line[0],
                                         name = line[1],
                                         price = line[3],
                                         image = line[2],
                                         release_date = line[4],
                                         lte_exists = line[5],
                                         slug = ''.join('_' if c == ' ' else c for c in line[1])
                )

