from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
     name = models.CharField(max_length= 255, null=True)
     email = models.EmailField(unique=True)
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = []

class Address(models.Model):
    user = models.ForeignKey(User, null=False, blank=False,on_delete=models.CASCADE)
    house_number = models.TextField(max_length = 255)
    street_name = models.TextField(max_length = 255)
    city = models.TextField(max_length = 255)
    county = models.TextField(max_length = 255)
    def __str__(self):
        return self.name
    
   

        

class Items(models.Model):
     types = (('trousers','trousers'),
              ('hoodies','hoodies'),
              ('joggers','joggers'),
              ('shirts','shirts'),
              ('headwear','headwear'),
              ('shorts','shorts'),
              ('jeans','jeans'),
              ('pants','pants'),
              ('chinos','chinos'),
              ('jackets','jackets'),
              )
     sizes = (
          ('XS','XS'),
          ('S','S'),
          ('M','M'),
          ('L','L'),
          ('XL','XL'),
          ('2XL','2XL'),
          ('3XL','3XL'),
          ('4XL','4XL'),
     )
     colors = (
          ('black','black'),
          ('white','white'),
          ('brown','brown'),
          ('green','green'),
          ('orange','orange'),
          ('burgundy','burgundy'),
          ('grey','grey'),
          ('red','red'),
          ('blue','blue'),
          ('cream','cream'),
     )
     name = models.TextField(max_length=50)
     price = models.DecimalField(decimal_places=2,max_digits=5)
     image1 = models.ImageField()
     image2 = models.ImageField(blank=True)
     image3 = models.ImageField(blank=True)
     color = models.CharField(max_length=50,choices = colors)
     size = models.CharField(max_length=20, choices=sizes)
     description = models.CharField(max_length=255, blank=True, null=True)
     category = models.TextField(max_length=255, default="nan", choices=types )
     def __str__(self):
        return self.name
     
class ItemView(models.Model):
    item = models.OneToOneField(Items, on_delete=models.CASCADE)
    def __str__(self):
       return self.name
    

     