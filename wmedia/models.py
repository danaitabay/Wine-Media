from django.db import models
from django.utils import timezone
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid

class Catagory(models.Model):

    type_name = models.CharField(max_length=20, help_text="Enter type of wine (e.g. Red wine, White wine, Rose)")
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.type_name

class Wine(models.Model):
    
    Brand_name = models.CharField(max_length=20)
    company_name = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because wine can only have one brand, but brands can have multiple wines
    Description = models.TextField(max_length=1000, help_text="Enter a brief description of the wine")
    types = models.ManyToManyField(Catagory, help_text="Select a type of wine")
    # ManyToManyField used because types can contain many wines. Wines can cover many types.
    # Catagory class has already been defined so we can specify the object above.
    bottled_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        
        return self.Brand_name
    
    
    def get_absolute_url(self):
        
        #Returns the url to access a particular wine instance.        
        return reverse('wine-detail', args=[str(self.id)])

    def display_catagory(self):
        """
        Creates a string for the types. This is required to display type in Admin.
        """
        return ', '.join([ types.type_name for types in self.types.all()[:3] ])
    display_catagory.short_description = 'Catagory'

class WineInstance(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular wine")
    wine = models.ForeignKey('Wine', on_delete=models.SET_NULL, null=True) 
    wine_type = models.CharField('Catagory', max_length=20, null=True)
    
    STOCK = (
        ('o', 'Out of stock'),
        ('a', 'Available'),
    )

    status = models.CharField(max_length=1, choices=STOCK, blank=True, default='a', help_text='Wine availability')

    class Meta:
        ordering = ["wine"]
        

    def __str__(self):
        
        #String for representing the Model object
        
        return '%s (%s)' % (self.wine.Brand_name, self.id)
    


class Company(models.Model):
    """
    Model representing the company.
    """
    company_name = models.CharField(max_length=20)
    established_date = models.DateField(null=True, blank=True)
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular company instance.
        """
        return reverse('company-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.company_name)