from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11,null=True)
    
    def __str__(self):
        return self.fname + " " + self.lname