# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Wine, Company, WineInstance, Catagory
from django.views import generic

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
class WineListView(generic.ListView):
    model = Wine
    #context_object_name = 'wine_list'   # your own name for the list as a template variable
    #queryset = Wine.objects #.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'wines/wine_list.html'  # Specify your own template name/location

class WineDetailView(generic.DetailView):
    model = Wine