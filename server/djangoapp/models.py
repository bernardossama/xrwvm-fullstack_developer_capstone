# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed
    def __str__(self):
        return self.name  # Return the name as the string representation

class CarModel(models.Model):
    CAR_TYPES = [
        ('sedan', 'Sedan'),
        ('suv','SUV'),
        ('wagon','Wagon'),
        ('hatchback','Hatchbak'),
        ('coupe','Coupe'),
        ('convertible','Convertible'),
        ('pickup','Pickup')
    ]
    car_make=models.ForeignKey(CarMake,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=12, choices=CAR_TYPES, default='sedan')
    year=models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2004)
        ])

    def __str__(self):
        return self.name    

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
