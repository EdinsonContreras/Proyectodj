from django.db import models

# Create your models here.
class Smartband(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)   
    age = models.IntegerField()
    weight=models.IntegerField()
    heart_rate=models.IntegerField()
    BPM=models.IntegerField()
    Sp_o=models.IntegerField()
    level_stress=models.IntegerField()
class meta:
    db_table="smartband"

