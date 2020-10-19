from django.db import models
from django.contrib.auth.models import User

from bonds.legal import get_Legal_Name


class Bond(models.Model):

    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    isin = models.CharField(max_length=50)
    size = models.IntegerField()
    currency = models.CharField(max_length=3)
    maturity = models.DateField()
    lei = models.CharField(max_length=50)
    legal_name = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
       
        legal_name = get_Legal_Name(self.lei)
            
        if legal_name != None:
            self.legal_name = legal_name.replace(" ", "")
        else:
            raise ValidationError("Legal name not found, please check LEI")
            
        super(Bond, self).save(*args, **kwargs)
