from django.core.management.base import BaseCommand
import pandas as pd
from crimeDetection.models import Victim

# python manage.py import_victim 'C:\\Users\\shyam\\OneDrive\\Desktop\\project\\Datathon\\Datathon\\crimeDetection\\management\\commands\\data\\VICTIM.xlsx'
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
            crime_name = row['CrimeGroup_Name']
            
            caste_name = row['Caste']
            
            fir_no = row['Crime_No']
            
            profession_name = row['Profession']
            
            age_value = row['age']

            # Create CrimeGroup instance linking District and Crime
            victim, created = Victim.objects.get_or_create(district=district_name, crime=crime_name, caste=caste_name, profession=profession_name, age=age_value, crime_no = fir_no)

            self.stdout.write(self.style.SUCCESS(f"Imported: {district_name} - {crime_name} - {caste_name} - {profession_name} - {age_value}"))

        self.stdout.write(self.style.SUCCESS("Data import completed."))
