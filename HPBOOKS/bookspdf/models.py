from django.db import models

# Create your models here.
class Potterheads(models.Model):
    name=models.CharField(max_length=25)
    emailid=models.EmailField()
    password=models.TextField(max_length=15)
    
    def __str__(self) -> str:
        return self.emailid
