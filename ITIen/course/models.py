from django.db import models

# Create your models here.
class Course(models.Model):
    ID=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=False)
    code=models.CharField(max_length=10, null=False)
    track=models.CharField(max_length=50, null=False)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Insert Date')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Update Date')
    
    def __str__(self):
        return self.name
