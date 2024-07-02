from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    qunatity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='car/media/images', blank=True, null=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"
    

class BuyCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='buycar')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bought {self.car.title} by {self.user.username} "


    

