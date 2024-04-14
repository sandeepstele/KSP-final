from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(District)
admin.site.register(CrimeGroup)
admin.site.register(CrimeGroupName)
admin.site.register(Cluster)
admin.site.register(CrimePercentage)
admin.site.register(Criminal)
admin.site.register(Victim)
admin.site.register(Victim_Crime)
admin.site.register(Criminal_Crime)
admin.site.register(Crime_correlation)
admin.site.register(Rowdy_sheeters)
