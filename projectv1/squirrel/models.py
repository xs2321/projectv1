# Create your models here.
from django.db import models

class Squirrel(models.Model):
    lat = models.FloatField()
    
    lon = models.FloatField()
    
    squirrel_id=models.CharField(
        max_length=100,
    )
    
    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = (
        (PM,'PM'),
        (AM,'AM'),
    )
    shift = models.CharField(
        max_length=16,
        choices=SHIFT_CHOICES,
    )
    
    date = models.DateField()
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile' 
    AGE_CHOICES = (
        (ADULT,'Adult'),
        (JUVENILE,'Juvenile'),
    )
    age = models.CharField(
        max_length=16,
        choices=AGE_CHOICES,
    )
    
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    PRI_COLOR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black' ),
    )
    pri_color = models.CharField(
        max_length=16,
        choices=PRI_COLOR_CHOICES,
        blank = True,
        null = True,
    )
    
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = (
        (GROUND_PLANE,'Ground Plane'),
        (ABOVE_GROUND,'Above Ground'),
    )
    location = models.CharField(
        max_length=30,
        choices=LOCATION_CHOICES,
        blank = True,
        null = True,
    )
    
    specific_location=models.CharField(
        max_length = 200,
        blank = True,
        null = True,
    )
    
    running = models.BooleanField(null=True)
    
    chasing = models.BooleanField(null=True)
    
    climbing = models.BooleanField(null=True)
    
    eating = models.BooleanField(null=True)

    foraging = models.BooleanField(null=True)
 
    other_activities = models.CharField(
        max_length = 200,
    )
    
    kuks = models.BooleanField(null=True)
 
    quaas = models.BooleanField(null=True)
    
    moans = models.BooleanField(null=True)

    tail_flags = models.BooleanField(null=True)

    tail_twitches = models.BooleanField(null=True)

    approaches = models.BooleanField(null=True)

    indifferent = models.BooleanField(null=True)
    
    runs_from = models.BooleanField(null=True)
    
    def __str__(self):
        return self.squirrel_id
