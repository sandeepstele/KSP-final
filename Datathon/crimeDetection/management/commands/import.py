from django.core.management.base import BaseCommand
import pandas as pd
from crimeDetection.models import District, CrimeGroup, Crime

# python manage.py import 'C:\\Users\\shyam\\OneDrive\\Desktop\\project\\Datathon\\Datathon\\crimeDetection\\management\\commands\\data\\BOOK1.xlsx'
class Command(BaseCommand):
    help = 'Imports data from an Excel file into the Django database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.import_data_from_excel(file_path)
    
    def import_data_from_excel(self, file_path):
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            # Get or create District instance
            district_name = row['District']
            district, created = District.objects.get_or_create(name=district_name)

            # Get or create Crime instance
            crime_name = row['Crime']
            crime, created = Crime.objects.get_or_create(name=crime_name)

            # Create CrimeGroup instance linking District and Crime
            crime_group = CrimeGroup.objects.create(name=crime_name, district=district)

            self.stdout.write(self.style.SUCCESS(f"Imported: {district_name} - {crime_name}"))

        self.stdout.write(self.style.SUCCESS("Data import completed."))
