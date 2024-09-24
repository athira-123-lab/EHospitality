from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=12)
    special=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    mobile=models.CharField(max_length=12)
    age=models.CharField(null=True)
    address=models.CharField(max_length=255)
    disease=models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Appointment(models.Model):
    name=models.CharField(max_length=12)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Prescription(models.Model):
    medicine=models.CharField(max_length=255)
    dosage=models.CharField(max_length=255)

    def __str__(self):
        return self.medicine


class Register(models.Model):

    name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)


    def __str__(self):
        return self.username