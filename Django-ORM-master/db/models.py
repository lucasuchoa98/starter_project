import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()


# Sample User model
class StudentData(models.Model):
    name = models.CharField(max_length=100)
    matricula = models.CharField(max_length=8,primary_key=True)
    cpf = models.CharField(max_length=9)
    #materia = models.ManyToManyField()

class MateriaData(models.Model):
    materia = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    
