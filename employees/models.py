from django.db import models

# Create your models here.
class Employee(models.Model):
    role=(
        (0,'manager'),
        (1,'supervisor'),
        (2,'Employee')
            )
    name=models.CharField(max_length=255,null=False)
    age=models.IntegerField()
    role=models.CharField(choices=role,default='empolyee',max_length=15)
    image=models.ImageField(upload_to='images/', default='1.jpg')
    ssn=models.CharField(max_length=14)