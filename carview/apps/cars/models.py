from django.db import models

class Car(models.Model):
    name=models.CharField('название', max_length=50)
    engine=models.CharField('харрактеристики двигателя', max_length=50)
    gear_type=models.CharField('какая КПП', max_length=50)
    type=models.CharField('тип кузова', max_length=50)
    type_drive_unit=models.CharField('какой привод', max_length=50)
    color=models.CharField('цвет авто', max_length=50)
    price=models.CharField('цена', max_length=50)
    year=models.CharField('год', max_length=50)