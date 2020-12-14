from django.shortcuts import render

# Create your views here.
from .models import Food, Table, TableInstance, Type, Drink

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tables = Table.objects.all().count()
    num_instances = TableInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = TableInstance.objects.filter(status__exact='a').count()
  # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=None)

from django.views import generic

class TableListView(generic.ListView):
    model = Table 
    paginate_by = 2
   
class TableDetailView(generic.DetailView):
    model = Table    

class FoodListView(generic.ListView):
    model = Food

class FoodDetailView(generic.DetailView):
    model = Food      

class DrinkListView(generic.ListView):
    model = Drink

class DrinkDetailView(generic.DetailView):
    model = Drink  
    