from django import forms
from .models import (
    ProductType, Product, Wilaya, Moughataa, Commune,
    PointOfSale, ProductPrice, Cart, CartProducts
)

class ExcelImportForm(forms.Form):
    OPERATION_CHOICES = [('import', 'Importer'), ('export', 'Exporter')]
    MODEL_CHOICES = [
        ('product_type', 'Types de Produits'),
        ('product', 'Produits'),
        ('wilaya', 'Wilayas'),
        ('moughataa', 'Moughataa'),
        ('commune', 'Communes'),
        ('point_of_sale', 'Points de Vente'),
        ('product_price', 'Prix des Produits'),
        ('cart', 'Paniers'),
        ('cart_product', 'Produits des Paniers'),
    ]
    
    operation = forms.ChoiceField(
        choices=OPERATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    
    model_type = forms.ChoiceField(
        choices=MODEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('operation') == 'import' and not cleaned_data.get('file'):
            raise forms.ValidationError("Un fichier est requis pour l'importation")
        return cleaned_data

# Model Forms
class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = '__all__'
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}

class WilayaForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = '__all__'

class MoughataaForm(forms.ModelForm):
    class Meta:
        model = Moughataa
        fields = '__all__'

class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = '__all__'

class PointOfSaleForm(forms.ModelForm):
    class Meta:
        model = PointOfSale
        fields = '__all__'
        widgets = {
            'gps_lat': forms.NumberInput(attrs={'step': '0.000001'}),
            'gps_lon': forms.NumberInput(attrs={'step': '0.000001'}),
        }

class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = '__all__'
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}

class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProducts
        fields = '__all__'
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }