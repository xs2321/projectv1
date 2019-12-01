# Create your models here.
from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    lat = models.FloatField(
        help_text = _('Latitude'),
        blank = True,
        null = True,
    )
    
    lon = models.FloatField(
        help_text = _('Longitude'),
        blank = True,
        null = True,
    )
    
    squirrel_id = models.CharField(
        max_length = 100,
        help_text = _('Unique Squirrel ID'),
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
        default=AM,
    )
    
    date = models.DateField(
        help_text = _('Date'),
    )
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile' 
    AGE_CHOICES = (
        (ADULT,'Adult'),
        (JUVENILE,'Juvenile'),
    )
    age = models.CharField(
        max_length=16,
        choices=AGE_CHOICES,
        blank = True,
        null = True,
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
        help_text = _('specific location of squirrel'),
    )
    
    running = models.BooleanField(
        blank = True,
        null = True,
    )
    
    chasing = models.BooleanField(
        blank = True,
        null = True,    
    )
    
    climbing = models.BooleanField(
        blank = True,
        null = True,
    )
    
    eating = models.BooleanField(
        blank = True,
        null = True,
    )
    
    foraging = models.BooleanField(
        blank = True,
        null = True,
    )
    
    other_activities = models.CharField(
        max_length = 200,
        blank = True,
        null = True,
    )
    
    kuks = models.BooleanField(
        blank = True,
        null = True,
    )
    
    quaas = models.BooleanField(
        blank = True,
        null = True, 
    )   
    
    moans = models.BooleanField(
        blank = True,
        null = True, 
    )

    tail_flags = models.BooleanField(
        blank = True,
        null = True,
    )

    tail_twitches = models.BooleanField(
        blank = True,
        null = True,
    )
    
    approaches = models.BooleanField(
        blank = True,
        null = True,
    )
    
    indifferent = models.BooleanField(
        blank = True,
        null = True,
    )
    
    runs_from = models.BooleanField(
        blank = True,
        null = True,
    )
    
    def __str__(self):
        return squirrel_id
