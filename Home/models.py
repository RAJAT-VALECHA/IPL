from django.db import models
from datetime import datetime
# Create your models here.
class Btresult(models.Model):
    Team1_Name=models.CharField(max_length = 122)
    Team2_Name=models.CharField(max_length = 122)
    Toss_Wining_Team=models.CharField(max_length = 122)
    Toss_Decision=models.CharField(max_length = 122)
    Venue=models.CharField(max_length = 122)
    ans = models.CharField(max_length = 122, default='100')
    date = models.DateField(default=datetime.today())

class Atresult(models.Model):
    Team1_Name=models.CharField(max_length = 122, default='100')
    Team2_Name=models.CharField(max_length = 122, default='100')
    T1_P1=models.CharField(max_length = 122)
    T1_P2=models.CharField(max_length = 122)
    T1_P3=models.CharField(max_length = 122)
    T1_P4=models.CharField(max_length = 122)
    T1_P5=models.CharField(max_length = 122)
    T1_P6=models.CharField(max_length = 122)
    T1_P7=models.CharField(max_length = 122)
    T1_P8=models.CharField(max_length = 122)
    T1_P9=models.CharField(max_length = 122)
    T1_P10=models.CharField(max_length = 122)
    T1_P11=models.CharField(max_length = 122)
    T2_P1=models.CharField(max_length = 122)
    T2_P2=models.CharField(max_length = 122)
    T2_P3=models.CharField(max_length = 122)
    T2_P4=models.CharField(max_length = 122)
    T2_P5=models.CharField(max_length = 122)
    T2_P6=models.CharField(max_length = 122)
    T2_P7=models.CharField(max_length = 122)
    T2_P8=models.CharField(max_length = 122)
    T2_P9=models.CharField(max_length = 122)
    T2_P10=models.CharField(max_length = 122)
    T2_P11=models.CharField(max_length = 122)
    Toss_Wining_Team=models.CharField(max_length = 122)
    Toss_Decision=models.CharField(max_length = 122)
    Venue=models.CharField(max_length = 122)
    ans = models.CharField(max_length = 122, default='100')
    date = models.DateField(default=datetime.today())
