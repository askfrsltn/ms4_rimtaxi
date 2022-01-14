from django.shortcuts import render
from .models import Tour

def all_tours(request):
    ''' A view to show all the tours on central page '''
    tours = Tour.objects.all()
    context = {
        'tours': tours,
    }
    return render(request, 'tours/tours.html', context)
