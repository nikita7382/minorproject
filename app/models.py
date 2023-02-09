from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 'xHTwM2nLXmsRBl1T16WSDv-CWDsAQAyWluR_RTSADTY'


class Viewer(AbstractUser):
    STATE_CHOICES=[
      ('Banke','Banke'),
      ('Bagmati','Bagmati'), 
      ('Bheri','Bheri'), 
      ('Dhawalagiri','Dhawalagiri'),
      ('Gandaki ','Gandaki'),
      ('Janakpur ','Janakpur '),
      ('Karnali','Karnali'),
      ('koshi','koshi') ,
      ('Lumbini','Lumbini'),
      ('Mahakali','Mahakali'), 
      ('Mechi','Mechi'),
      ('Narayani','Narayani'),
      ('Rapti','Rapti'),
      ('Sagarmatha','Sagarmatha'),
      ('seti','seti')
    ]
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True)
    age=models.IntegerField(null=True)
    location=models.CharField(choices=STATE_CHOICES,max_length=50)

    REQUIRED_FIELDS=[]


class Movie(models.Model):
    movie_id=models.IntegerField()
    title = models.CharField(max_length=200,null=True)
    overview=models.TextField(null=True)
    genres = models.CharField(max_length=200,null=True)
    casts = models.CharField(max_length = 200,null=True)
    crew = models.CharField(max_length=50,null=True)
    tags = models.CharField(max_length=1000,null=True)
    # poster = models.ImageField(upload_to='poster')
    # description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Myrating(models.Model):
    user = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0, validators=[MaxValueValidator(5),
                               MinValueValidator(0)],)


class MyList(models.Model):
    user = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # watch = models.BooleanField(default=False)
