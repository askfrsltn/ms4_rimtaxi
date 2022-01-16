from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class City(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class Car(models.Model):
    car_name = models.CharField(max_length=10)
    car_friendly_name = models.CharField(max_length=254)
    car_model = models.CharField(max_length=254)
    car_pax = models.DecimalField(max_digits=1, decimal_places=0)
    car_class = models.CharField(max_length=254)
    car_premium = models.DecimalField(max_digits=3, decimal_places=0)
    car_image = models.ImageField(null=True, blank=True)
    car_image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.car_class

    def get_friendly_name(self):
        return self.car_friendly_name


class Tour(models.Model):
    tour_name = models.CharField(max_length=254)
    tour_friendly_name = models.CharField(max_length=254)
    tour_description = models.TextField()
    tour_price = models.DecimalField(max_digits=5, decimal_places=2)
    tour_distance = models.DecimalField(max_digits=3, decimal_places=0)
    tour_duration = models.DecimalField(max_digits=3, decimal_places=0)
    tour_theme = models.ForeignKey(
        'Theme', null=True, blank=True, on_delete=models.SET_NULL)
    tour_city = models.ForeignKey(
        'City', null=True, blank=True, on_delete=models.SET_NULL)
    tour_ranking = models.DecimalField(max_digits=3, decimal_places=2)
    tour_image_url = models.URLField(max_length=1024, null=True, blank=True)
    tour_image = models.ImageField(null=True, blank=True)
    tour_isspecialoffer = models.BooleanField()
    tour_specialoffer = models.CharField(max_length=100, null=True, blank=True)
    tour_specialoffer_discount = models.DecimalField(
        max_digits=2, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.tour_friendly_name


class Review(models.Model):
    '''change to models.DateField(auto_now=True,
    auto_now_add=False) after intial download'''
    review_date = models.CharField(max_length=24)
    review_order_id = models.CharField(max_length=6)
    review_order_date = models.CharField(max_length=24)
    review_customer_id = models.CharField(max_length=84)
    review_tour_id = models.ForeignKey(
        'Tour', null=True, blank=True, on_delete=models.SET_NULL)
    review_ranking = models.DecimalField(max_digits=2, decimal_places=2)
    review_text = models.TextField()

    def __str__(self):
        return self.review_order_id
