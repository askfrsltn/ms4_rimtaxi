from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Tour, City, Theme
from django.contrib import messages
from django.db.models import Q


def all_tours(request):
    ''' A view to show all the tours on central page '''

    tours = Tour.objects.all()
    query = None
    cities = None
    themes = None
    specialoffer = None

    if request.GET:
        # query tours by theme
        
        if 'theme' in request.GET:
            themes = request.GET['theme']
            theme = Theme.objects.get(name=themes)
            tours = tours.filter(tour_theme=theme)
        
        # query tours by city
        if 'city' in request.GET:
            cities = request.GET['city']
            city = City.objects.get(name=cities)
            tours = tours.filter(tour_city=city)
        
        # query tours by special offer deal
        if 'specialoffer' in request.GET:
            specialoffer = request.GET['specialoffer']
            tours = tours.filter(tour_specialoffer=specialoffer)

        # search query tours by name and description
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search defined")
                return redirect(reverse('tours'))

            queries = Q(tour_friendly_name__icontains=query) | \
                Q(tour_description__icontains=query)
            tours = tours.filter(queries)

    context = {
        'tours': tours,
        'search_term': query,
        'current_cities': cities,
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):

    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_detail.html', context)
