from django.db import models  
class Diary(models.Model):  
    did = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=100)  
    middle_name = models.CharField(max_length=100)  
    last_names = models.CharField(max_length=100)
    email = models.EmailField()  
    cellphone = models.CharField(max_length=15)  
    class Meta:  
        db_table = "diary"  