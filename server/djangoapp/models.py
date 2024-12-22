from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # You can add other fields as needed, like a logo, country of origin, etc.
    
    def __str__(self):
        return self.name  # Return the name as the string representation

# CarModel model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # You can add more types here
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )
    
    # You can add other fields such as engine type, color options, etc.
    
    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Return both car make and car model as string representation
