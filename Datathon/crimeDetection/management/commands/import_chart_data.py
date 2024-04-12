from django.core.management.base import BaseCommand
from crimeDetection.models import CrimeGroupName, Cluster, CrimePercentage
import pandas as pd

# python manage.py import_chart_data 'C:\\Users\\shyam\\OneDrive\\Desktop\\project\\Datathon\\Datathon\\crimeDetection\\management\\commands\\data\\BOOK2.xlsx'
class Command(BaseCommand):
    help = 'Import data from an Excel file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        import_data_from_excel(file_path)
        
def import_data_from_excel(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Get or create CrimeGroup instance
        crime_group_name = row['CrimeGroup_Name']
        crime_group, created = CrimeGroupName.objects.get_or_create(name=crime_group_name)

        # Get or create Cluster instance
        cluster_number = row['ClusterNo']
        cluster, created = Cluster.objects.get_or_create(number=cluster_number)

        # Create CrimePercentage instance
        percentage_value = row['percentage_specific_crime_per_cluster_y']
        crime_percentage = CrimePercentage.objects.create(crime_group=crime_group, cluster=cluster, percentage=percentage_value)

        print(f"Imported: {crime_group_name} - Cluster {cluster_number} - Percentage: {percentage_value}%")

    print("Data import completed.")
