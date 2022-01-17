from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Tour, City, Theme, Review
from django.contrib import messages
from django.db.models import Q


def all_tours(request):
    ''' A view to show all the tours on central page '''

    tours = Tour.objects.all()
    query = None
    cities = None
    themes = None
    specialoffer = None
    sort = None
    direction = None

    if request.GET:
        # sort tours by price
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tours = tours.annotate('name')

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tours = tours.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'
    context = {
        'tours': tours,
        'search_term': query,
        'current_cities': cities,
        'current_sorting': current_sorting,
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    reviews = Review.objects.all()
    tour_reviews = reviews.filter(review_tour_id=tour_id)
    print(tour_reviews)
    
    context = {
        'tour': tour,
        'tour_reviews': tour_reviews,
    }
    return render(request, 'tours/tour_detail.html', context)
