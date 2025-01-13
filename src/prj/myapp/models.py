from django.db import models
from geopy.geocoders import Nominatim

class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    label = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.label


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    unit_measure = models.CharField(max_length=45)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Wilaya(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=252)

    def __str__(self):
        return self.name


class Moughataa(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    label = models.CharField(max_length=45)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class Commune(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PointOfSale(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.gps_lat or not self.gps_lon:
            # Supposons que `commune` a une adresse ou une ville
            address = self.commune.get_full_address()  # Assurez-vous que la commune peut renvoyer une adresse
            lat, lon = get_lat_lon_from_address(address)
            if lat and lon:
                self.gps_lat = lat
                self.gps_lon = lon
        super().save(*args, **kwargs)





class ProductPrice(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    point_of_sale = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.value}"


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class CartProducts(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.cart.name} - {self.product.name}"
