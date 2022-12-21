from django.db import models

# Create your models here.

class Reporteria(models.Model):
    id_repor = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True)
    product_name = models.CharField(max_length=50, blank=True)
    slug = models.CharField(max_length=50, blank=True)
    accion = models.CharField(max_length=50, blank = True)
    create_date = models.DateField(auto_now_add =True)
    hora = models.TimeField(auto_now_add =True)
    stock  = models.IntegerField()


