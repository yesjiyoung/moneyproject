from django.db import models
from django.utils.timezone import now

# Create your models here.

class Money(models.Model):

    #memeber = (('지영','지영'), ('혜선','혜선'), ('시현','시현'), ('민정','민정'), ('성필','성필'), ('정규','정규'),('현수','현수'),('슬옹','슬옹'),('기려','기려'),('세아','세아'),('성학','성학'),('태원','태원'),('지윤','지윤'),('시은','시은'),('도형','도형'))
    name = models.CharField(max_length = 5) #choices = memeber)
    deposit = models.IntegerField(default = 0)
    withdraw = models.IntegerField(default = 0)
    input_date = models.DateTimeField(default = now)

    def __str__(self):
        return self.name
