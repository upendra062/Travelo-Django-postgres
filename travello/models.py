from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)



    # id: int #it will create automatically a id/primary key for you no need to give
    # name: str
    # img: str
    # desc: int
    # price: int
    # offer: bool
