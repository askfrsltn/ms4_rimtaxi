from django.shortcuts import render


# Create your views here.
def view_trip(request):
    ''' A view for trip content '''
    return render(request, 'trip/trip.html')
