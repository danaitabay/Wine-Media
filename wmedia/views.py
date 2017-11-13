# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Wine, Company, WineInstance, Catagory

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_wines=Wine.objects.all().count()
    num_instances=WineInstance.objects.all().count()
    # Available wines (status = 'a')
    num_instances_available=WineInstance.objects.filter(status__exact='a').count()
    num_companies=Company.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_wines':num_wines,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_Companies':num_companies},
    )