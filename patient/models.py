from django.db import models

class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1) # M,F
    birth_date = models.DateField()
    phone = models.CharField(max_length=20, blank=True, null=True) 
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True) 
    registration_date = models.DateField()
    diagnosis = models.TextField(blank=True, null=True) 

    class Meta:
    
        pass 

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.patient_id})"