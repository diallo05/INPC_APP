from django.db import models

# Create your models here.
from django.db import models
from geopy.geocoders import Nominatim

# Modèle pour les produits
class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    categorie = models.CharField(max_length=50)
    unite = models.CharField(max_length=20)

    def __str__(self):
        return self.description

# Modèle pour les points de vente
class PointVente(models.Model):
    id_point = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    commune = models.CharField(max_length=100)
    categorie = models.CharField(max_length=50)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        # Utilisation de Geopy pour obtenir la latitude et la longitude à partir de l'adresse (localisation)
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(self.localisation)

        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude
        else:
            self.latitude = None
            self.longitude = None

        super(PointVente, self).save(*args, **kwargs)

# Modèle pour les paniers
class Panier(models.Model):
    id_panier = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    categorie = models.CharField(max_length=50)

    def __str__(self):
        return self.description

# Modèle pour la relation entre produit et panier avec pondération
class ProduitPanier(models.Model):
    id_produitpanier = models.AutoField(primary_key=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    ponderation = models.FloatField()

    def __str__(self):
        return f"{self.produit.description} - {self.panier.description}"

# Modèle pour la relation entre produit et point de vente avec prix et date
class ProduitPointVente(models.Model):
    id_produitvente = models.AutoField(primary_key=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    point_vente = models.ForeignKey(PointVente, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    frequence_actualisation = models.CharField(max_length=50, choices=[
        ('mensuel', 'Mensuel'),
        ('trimestriel', 'Trimestriel'),
        ('annuel', 'Annuel'),
        ('autre', 'Autre')
    ], default='mensuel')

    def __str__(self):
        return f"{self.produit.description} - {self.point_vente.description} - {self.date}"


# Modèle pour l'indice
class Indice(models.Model):
    id_indice = models.AutoField(primary_key=True)
    date_periode = models.DateField()
    commune = models.CharField(max_length=100)
    valeur_indice = models.FloatField()

    def __str__(self):
        return f"Indice {self.commune} - {self.date_periode} : {self.valeur_indice}"


class SocioEconomique(models.Model):
    id_socio = models.AutoField(primary_key=True)
    commune = models.CharField(max_length=100, unique=True)
    revenu_moyen = models.DecimalField(max_digits=12, decimal_places=2)
    taux_chomage = models.DecimalField(max_digits=5, decimal_places=2)
    population = models.IntegerField()
    annee = models.IntegerField()

    def __str__(self):
        return f"Socio-économique {self.commune} - {self.annee}"


class HistoriquePonderation(models.Model):
    id_historique = models.AutoField(primary_key=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    ponderation = models.FloatField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.produit.description} - {self.panier.description} - {self.date_debut}"
