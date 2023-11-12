from django.db import models

# Create your models here.
class District(models.Model):
    district_name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return '{}'.format(self.district_name)
class Branch(models.Model):
    branch_name=models.CharField(max_length=250,unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.branch_name)
