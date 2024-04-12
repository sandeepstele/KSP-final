from django.core.management.base import BaseCommand
from crimeDetection.models import District, CrimeGroup


class Command(BaseCommand):
    help = 'Import data from text files into District and CrimeGroup models'

    def handle(self, *args, **kwargs):
        # Read district names from the text file
        with open('C:\\Users\\shyam\\OneDrive\\Desktop\\project\\Datathon\\Datathon\\crimeDetection\\management\\commands\\data\\output4.txt', 'r') as file:

            district_names = [line.strip() for line in file.readlines()]

        # Create District instances and save them to the database
        for name in district_names:
            district, _ = District.objects.get_or_create(name=name)

        # Read crime group names from the text file
        with open('C:\\Users\\shyam\\OneDrive\\Desktop\\project\\Datathon\\Datathon\\crimeDetection\\management\\commands\\data\\output3.txt', 'r') as file:

            crime_group_names = [line.strip() for line in file.readlines()]

        # Create CrimeGroup instances and associate them with districts
        for name in crime_group_names:
            district = District.objects.order_by('?').first()  # Randomly select a district
            crime_group, _ = CrimeGroup.objects.get_or_create(name=name, district=district)

        self.stdout.write(self.style.SUCCESS('Data import completed successfully'))
