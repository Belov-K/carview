from django.db import models

class Car(models.Model):
    name=models.CharField('название', max_length=50)
    engine_power=models.IntegerField('мощность двигателя', blank=True, null=True)
    engine_volume=models.FloatField('обьем двигателя', blank=True, null=True)
    engine_type=models.CharField('какое топливо', max_length=50)
    gear_type=models.CharField('какая КПП', max_length=50)
    type=models.CharField('тип кузова', max_length=50)
    type_drive_unit=models.CharField('какой привод', max_length=50)
    color=models.CharField('цвет авто', max_length=50)
    price=models.IntegerField('цена', blank=True, null=True)
    year=models.IntegerField('год', blank=True, null=True)