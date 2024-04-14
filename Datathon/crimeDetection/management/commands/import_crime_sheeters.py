from django.core.management.base import BaseCommand
import pandas as pd
from crimeDetection.models import Rowdy_sheeters

# python manage.py import_crime_sheeters 'C:\\Users\\shyam\\OneDrive\\Desktop\\project\\KSP-final\\Datathon\\crimeDetection\\management\\commands\\data\\ROWDY.xlsx'
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
            district_name = row['District_Name']

            # Get or create Crime instance
            category = row['Rowdy_Category']
            
            rowdy_no = row['Rowdy_Sheet_No']
            
            age_value = row['Age'] 
            # Create CrimeGroup instance linking District and Crime
            rowdy_sheeters, created = Rowdy_sheeters.objects.get_or_create(district=district_name, category=category, rowdy_no = rowdy_no,age = age_value)

            self.stdout.write(self.style.SUCCESS(f"Imported:{category} - {district_name} - {rowdy_no}"))

        self.stdout.write(self.style.SUCCESS("Data import completed."))
