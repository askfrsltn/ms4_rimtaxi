from django.shortcuts import render, redirect


# Create your views here.
def view_trip(request):
    ''' A view for trip content '''
    return render(request, 'trip/trip.html')


def add_to_trip(request, tour_id):
    pax = int(request.POST.get('pax'))
    car_class = request.POST.get('car_class')
    departure_date = request.POST.get('departure_date')
    departure_address = request.POST.get('departure_address')
    redirect_url = request.POST.get('redirect_url')

    trip = request.session.get("trip", {})
    if tour_id in list(trip.keys()):
        trip[tour_id] += pax
    else: 
        trip[tour_id] = pax

    request.session['trip'] = trip
    print(request.session['trip'])
    return redirect(redirect_url)
