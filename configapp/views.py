from django.shortcuts import render
from .models import Category, Regions, District, Neighbourhood


def all_data_view(request):
    categories = Category.objects.all()
    regions = Regions.objects.all()
    districts = District.objects.all()
    neighbourhoods = Neighbourhood.objects.all()

    context = {
        'categories': categories,
        'regions': regions,
        'districts': districts,
        'neighbourhoods': neighbourhoods,
    }
    return render(request, 'all_data.html', context)
