# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Wine, Company, WineInstance, Catagory
from django.views import generic
from django.template.loader import get_template
from django.template import Context
from django.template.context_processors import csrf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def login(request):
    c = {}
    c.update(csrf(request))
    return render('login.html', c) 

@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_wines=Wine.objects.all().count()
    num_instances=WineInstance.objects.all().count()
    # Available wines (status = 'a')
    num_instances_available=WineInstance.objects.filter(status__exact='a').count()
    num_companies=Company.objects.all().count()  # The 'all()' is implied by default.
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_wines':num_wines,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_companies':num_companies, 'num_visits':num_visits},
    )
class WineListView(LoginRequiredMixin, generic.ListView):
    model = Wine
    #context_object_name = 'wine_list'   # your own name for the list as a template variable
    #queryset = Wine.objects #.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'wines/wine_list.html'  # Specify your own template name/location
    paginate_by = 10
    
class WineDetailView(generic.DetailView):
    model = Wine
    template_name = 'wines/wine-detail.html' 

class CompanyListView(LoginRequiredMixin, generic.ListView):
    model = Company
    #context_object_name = 'wine_list'   # your own name for the list as a template variable
    #queryset = Wine.objects #.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'company/company_list.html'  # Specify your own template name/location
    paginate_by = 10
    
class CompanyDetailView(generic.DetailView):
    model = Company
    template_name = 'company/company-detail.html' 

class MyWineByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing MyWine per current user. 
    """
    model = WineInstance
    template_name ='wines/wineinstance_list_per_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return WineInstance.objects.filter(owner=self.request.user)