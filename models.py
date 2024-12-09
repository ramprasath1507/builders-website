from django.db import models

class contractor(models.Model):
    contractor_id = models.AutoField
    contractor_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=50, default="")
    phoneno = models.IntegerField()
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.category