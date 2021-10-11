from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f' {self.name} {self.address}'

class Participant(models.Model):
    email = models.EmailField(unique=True)
    name= models.CharField(max_length=200)

    def __str__(self):
        return f' {self.name} - {self.email} '

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    owner_email = models.EmailField(default='test@example.com')
    date = models.DateField(default='2021-10-09')
    image = models.ImageField(upload_to='images')
    # set a one to many relationship between two models
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)  
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    # blank true means that we can let this field empty in the admin form when we create a new instance
    # null true means that the database table can hold a nullable value

    # with this, we tell django how it have to represent in string format an instance of this model
    def __str__(self):
        # return f'{self.title}-{self.description}'
        return f' {self.title} '
