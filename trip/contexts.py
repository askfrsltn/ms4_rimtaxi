from decimal import Decimal
from django.conf import settings


def trip_contents(request):
    # set up variables to calculate discount
    trip_items = []
    discount_items = []
    trip_count = 0
    discount_base = 0
    discount = 0
    total = 0

    # condiction to set up discount -REWORK LOOP!!!
    if trip_count > settings.TRIP_DISCOUNT_THRESHOLD:
        trip_count = len(trip_items)
        # sum(trip_item['tour_price'] for trip_item in trip_items)
        total = 0 
        discount_base = 0
        discount = discount_base*Decimal(settings.TRIP_DISCOUNT_PERCENTAGE)/100
        # grand_total = sum(trip_items)-discount
    else:
        discount = 0

    grand_total = total+discount
    context = {
        'trip_items': trip_items,
        'total': total,
        'trip_count': trip_count,
        'discount': discount,
        'grand_total': grand_total,
        'trip_discount_percentage': settings.TRIP_DISCOUNT_PERCENTAGE,
        'trip_discount_threshold': settings.TRIP_DISCOUNT_THRESHOLD,
    }
    return context
