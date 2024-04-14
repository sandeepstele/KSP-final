from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Victim(models.Model):
    district = models.CharField(max_length=100)
    crime = models.CharField(max_length=100)
    caste = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    crime_no = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.crime}-{self.district}-{self.profession}"

class Victim_Crime(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return f"{self.name}"

class Crime_correlation(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return f"{self.name}"

class Criminal(models.Model):
    crime = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    crime_no = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.crime}-{self.district}-{self.profession}"

class Rowdy_sheeters(models.Model):
    district = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    rowdy_no = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.category}-{self.district}-{self.rowdy_no}"
    

class Criminal_Crime(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Crime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CrimeGroup(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='crime_groups')

    def __str__(self):
        return self.name

class CrimeGroupName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cluster(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number)

class CrimePercentage(models.Model):
    crime_group = models.ForeignKey(CrimeGroupName, on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.crime_group} - Cluster {self.cluster}: {self.percentage}%"
