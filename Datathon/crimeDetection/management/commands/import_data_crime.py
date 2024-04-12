from django.core.management.base import BaseCommand
from crimeDetection.models import Victim_Crime


class Command(BaseCommand):
    help = 'Import data from text files into District and CrimeGroup models'

    def handle(self, *args, **kwargs):
        # Read district names from the text file
        with open('C:\\Users\\shyam\\OneDrive\\Desktop\\project\\Datathon\\Datathon\\crimeDetection\\management\\commands\\data\\unique4.txt', 'r') as file:

            district_names = [line.strip() for line in file.readlines()]

        # Create District instances and save them to the database
        for name in district_names:
            victim_crime, _ = Victim_Crime.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Data import completed successfully'))