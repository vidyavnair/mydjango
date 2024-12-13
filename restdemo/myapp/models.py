from django.db import models

# # Create your models here.
class Full_data(models.Model):

     username=models.CharField(max_length=200)
     phone=models.IntegerField()

     class Meta():
         def __str__(self) -> str:
             
              return self.Name
