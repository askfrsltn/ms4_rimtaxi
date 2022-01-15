from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Tour
from django.db.models import Q


def all_tours(request):
    ''' A view to show all the tours on central page '''

    tours = Tour.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                massages.error(request, "No search defined")
                return redirect(reverse('tours'))

            queries = Q(tour_friendly_name__icontains=query)|Q(tour_description__icontains=query)
            tours = tours.filter(queries)

    context = {
        'tours': tours,
        'search_term': query,
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):
    
    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_detail.html', context)
