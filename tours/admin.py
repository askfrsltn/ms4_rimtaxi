from django.contrib import admin
from .models import Tour, Theme, City, Car, Review

# Register your models here.
admin.site.register(City)
admin.site.register(Theme)
admin.site.register(Car)
admin.site.register(Tour)
admin.site.register(Review)
