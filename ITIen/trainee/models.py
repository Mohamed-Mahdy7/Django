from django.db import models

# Create your models here.

class Trainee(models.Model):
    ID=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=False)
    age=models.IntegerField(null=False)
    degree=models.DecimalField(decimal_places=2, max_digits=4 ,null=False)
    
    def __str__(self):
        return self.name