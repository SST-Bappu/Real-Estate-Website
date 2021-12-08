from django.db import models
from datetime import datetime
# Create your models here.

class realtors(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255,unique=True)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table="realtors"