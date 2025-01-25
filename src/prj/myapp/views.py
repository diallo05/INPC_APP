from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Count  # Ajoutez cette ligne d'importation
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta


# Create your views here.
@login_required
def home(request):
    return render(request, 'base.html')


class productListView(LoginRequiredMixin,ListView):
    model=Product
    template_name='product_list.html'
    context_object_name='product_list'

class productDetailView(LoginRequiredMixin,DetailView):
    model=Product
    template_name='product_detail.html'
    context_object_name='product'

class productCreateView(LoginRequiredMixin,CreateView):
    model=Product
    template_name='product_form.html'
    fields='__all__'
    success_url = reverse_lazy('product_list')

class productUpdateView(LoginRequiredMixin, UpdateView):
    model=Product
    template_name='product_form.html'
    fields='__all__'
    success_url = reverse_lazy('product_list')

class productDeleteView(LoginRequiredMixin,DeleteView):
    model=Product
    template_name='product_confirm_delete.html'
    success_url='/'
class pointVenteListView(LoginRequiredMixin,ListView):
    model=PointOfSale
    template_name='pointvente.html'
    context_object_name='pointVente_list'

class ProductpriceListView(LoginRequiredMixin,ListView):
    model=ProductPrice
    template_name='productprice_list.html'
    context_object_name='productprice_list'
class ProductpriceDetailView(LoginRequiredMixin,DetailView):
    model=ProductPrice
    template_name='productprice_detail.html'
    context_object_name='productprice'

class ProductpriceCreateView(LoginRequiredMixin,CreateView):
    model=ProductPrice
    template_name='productprice_form.html'
    fields='__all__'
    success_url = reverse_lazy('product_list')
class ProductpriceUpdateView(LoginRequiredMixin,UpdateView):
    model=ProductPrice
    template_name='productprice_form.html'
    fields='__all__'

class ProductpriceDeleteView(LoginRequiredMixin,DeleteView):
    model=ProductPrice
    template_name='productprice_confirm_delete.html'
    success_url='/'



class pointVenteDetailView(LoginRequiredMixin,DetailView):
    model=PointOfSale
    template_name='pointvente_detail.html'
    context_object_name='pointVente'

class pointVenteCreateView(LoginRequiredMixin,CreateView):
    model=PointOfSale
    template_name='pointvente_form.html'
    fields='__all__'
    success_url = reverse_lazy('pointVente_list')

class pointVenteUpdateView(LoginRequiredMixin,UpdateView):
    model=PointOfSale
    template_name='pointVente_form.html'
    fields='__all__'

class pointVenteDeleteView(LoginRequiredMixin,DeleteView):
    model=PointOfSale
    template_name='pointVente_confirm_delete.html'
    success_url='/'

class wilayaListView(LoginRequiredMixin,ListView):
    model = Wilaya
    template_name = 'wilaya_list.html'
    context_object_name = 'wilaya_list'

class wilayaDetailView(LoginRequiredMixin,DetailView): 
    model=Wilaya
    template_name='wilaya_details.html'
    context_object_name='wilaya'

class wilayaCreateView(LoginRequiredMixin,CreateView):
    model=Wilaya
    template_name='wilaya_form.html'
    fields='__all__'
    success_url = reverse_lazy('pointVente_list')

class wilayaUpdateView(LoginRequiredMixin,UpdateView):
    model=Wilaya
    template_name='wilaya_form.html'
    fields='__all__'    

class wilayaDeleteView(LoginRequiredMixin,DeleteView):
    model=Wilaya
    template_name='wilaya_confirm_delete.html'
    success_url='/'

class moughataaListView(LoginRequiredMixin,ListView):
    model=Moughataa
    template_name='moughataa_list.html'
    context_object_name='moughataa_list'

class moughataaDetailView(LoginRequiredMixin,DetailView):
    model=Moughataa
    template_name='moughataa_detail.html'
    context_object_name='moughataa'

class moughataaCreateView(LoginRequiredMixin,CreateView):
    model=Moughataa
    template_name='moughataa_form.html'
    fields='__all__'
    success_url = reverse_lazy('pointVente_list')

class moughataaUpdateView(LoginRequiredMixin,UpdateView):  
    model=Moughataa
    template_name='moughataa_form.html'
    fields='__all__'

class moughataaDeleteView(LoginRequiredMixin,DeleteView):
    model=Moughataa
    template_name='moughataa_confirm_delete.html'
    success_url='/'

class communeListView(LoginRequiredMixin,ListView):
    model=Commune
    template_name='commune_list.html'
    context_object_name='commune_list'  

class communeDetailView(LoginRequiredMixin,DetailView):
    model=Commune
    template_name='commune_detail.html'
    context_object_name='commune'

class communeCreateView(LoginRequiredMixin,CreateView):
    model=Commune
    template_name='commune_form.html'
    fields='__all__'
    success_url = reverse_lazy('commune_list')

class communeUpdateView(LoginRequiredMixin,UpdateView):
    model=Commune
    template_name='commune_form.html'
    fields='__all__'

class communeDeleteView(LoginRequiredMixin,DeleteView):
    model=Commune
    template_name='commune_confirm_delete.html'
    success_url='/'

class productTypeListView(LoginRequiredMixin,ListView):
    model=ProductType
    template_name='producttype_list.html'
    context_object_name='productType_list'

class productTypeDetailView(LoginRequiredMixin,DetailView):
    model=ProductType
    template_name='producttype_details.html'
    context_object_name='productType'

class productTypeCreateView(LoginRequiredMixin,CreateView):
    model=ProductType
    template_name='producttype_form.html'
    fields='__all__'
    success_url = reverse_lazy('productType_list')

class productTypeUpdateView(LoginRequiredMixin,UpdateView):
    model=ProductType
    template_name='producttype_form.html'
    fields='__all__'

class productTypeDeleteView(LoginRequiredMixin,DeleteView):
    model=ProductType
    template_name='producttype_confirm_delete.html'
    success_url='/'

class CartView(LoginRequiredMixin,ListView):
    model=Cart
    template_name='cart_list.html'
    context_object_name='cart_list'

class CartDetailView(LoginRequiredMixin,DetailView):
    model=Cart
    template_name='cart_details.html'
    context_object_name='cart'

class CartCreateView(LoginRequiredMixin,CreateView):
    model=Cart
    template_name='cart_form.html'
    fields='__all__'
    success_url = reverse_lazy('cart_list')

class CartUpdateView(LoginRequiredMixin,UpdateView):        
    model=Cart
    template_name='cart_form.html'
    fields='__all__'

class CartDeleteView(LoginRequiredMixin,DeleteView):    
    model=Cart
    template_name='cart_confirm_delete.html'
    success_url='/'

class CartProductsView(LoginRequiredMixin,ListView):
    model=CartProducts
    template_name='cartproduct_list.html'
    context_object_name='cartproduct_list'

class CartProductDetailView(LoginRequiredMixin,DetailView):
    model=CartProducts
    template_name='cartproduct_details.html'
    context_object_name='cartProduct'

class CartProductCreateView(LoginRequiredMixin,CreateView):
    model=CartProducts
    template_name='cartproduct_form.html'
    fields='__all__'
    success_url = reverse_lazy('cartproduct_list')

class CartProductUpdateView(LoginRequiredMixin,UpdateView):        
    model=CartProducts
    template_name='cartproduct_form.html'
    fields='__all__'

class CartProductDeleteView(LoginRequiredMixin,DeleteView):    
    model=CartProducts
    template_name='cart_confirm_delete.html'
    success_url='/'

@login_required
def import_wilaya(request, Wilaya):
    if request.method == 'POST':
        file = request.FILES['formFile']
        try:
            df = pd.read_excel(file)
            model = globals()[Wilaya]
            for index, row in df.iterrows():
                model.objects.create(**row.to_dict())
            messages.success(request, 'Data imported successfully!')
        except Exception as e:
            messages.error(request, f'Error importing data: {e}')
        return redirect(f'{Wilaya.lower()}_list')
    return render(request, 'import.html', {'oname': Wilaya, 'opath': Wilaya.lower()})
@login_required
def export_wilaya(request, Wilaya):
    model = globals()[Wilaya]
    data = model.objects.all().values()
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename={Wilaya.lower()}_export.xlsx'
    df.to_excel(response, index=False)
    return response

@login_required
def import_moughataa(request):
    if request.method == 'POST':
        file = request.FILES['formFile']
        try:
            df = pd.read_excel(file)
            for index, row in df.iterrows():
                # Récupérer le code de la wilaya depuis le fichier Excel
                wilaya_code = row['wilaya']  # Assurez-vous que la colonne s'appelle 'wilaya' dans le fichier Excel
                
                # Trouver l'instance de Wilaya correspondante
                try:
                    wilaya_instance = Wilaya.objects.get(code=wilaya_code)
                except Wilaya.DoesNotExist:
                    messages.error(request, f'Wilaya avec le code {wilaya_code} n\'existe pas.')
                    continue  # Passer à la ligne suivante si la Wilaya n'existe pas
                
                # Créer l'instance de Moughataa avec l'instance de Wilaya
                Moughataa.objects.create(
                    code=row['code'],  # Assurez-vous que la colonne s'appelle 'code' dans le fichier Excel
                    label=row['label'],  # Assurez-vous que la colonne s'appelle 'label' dans le fichier Excel
                    wilaya=wilaya_instance
                )
            messages.success(request, 'Données importées avec succès !')
        except Exception as e:
            messages.error(request, f'Erreur lors de l\'importation des données : {e}')
        return redirect('moughataa_list')  # Rediriger vers la liste des Moughataa
    return render(request, 'import.html', {'oname': 'Moughataa', 'opath': 'moughataa'})
@login_required
def export_moughataa(request, Moughataa):
    model = globals()[Moughataa]
    data = model.objects.all().values()
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename={Moughataa.lower()}_export.xlsx'
    df.to_excel(response, index=False)
    return response


@login_required
def import_cart(request, Cart):
    if request.method == 'POST':
        file = request.FILES['formFile']
        try:
            df = pd.read_excel(file)
            model = globals()[Cart]
            for index, row in df.iterrows():
                model.objects.create(**row.to_dict())
            messages.success(request, 'Data imported successfully!')
        except Exception as e:
            messages.error(request, f'Error importing data: {e}')
        return redirect(f'{Cart.lower()}_list')
    return render(request, 'import.html', {'oname': Cart, 'opath': Cart.lower()})
@login_required
def export_cart(request, Cart):
    model = globals()[Cart]
    data = model.objects.all().values()
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename={Cart.lower()}_export.xlsx'
    df.to_excel(response, index=False)
    return response
@login_required
def import_producttype(request, ProductType):
    if request.method == 'POST':
        file = request.FILES['formFile']
        try:
            df = pd.read_excel(file)
            model = globals()[ProductType]
            for index, row in df.iterrows():
                model.objects.create(**row.to_dict())
            messages.success(request, 'Data imported successfully!')
        except Exception as e:
            messages.error(request, f'Error importing data: {e}')
        return redirect(f'{Cart.lower()}_list')
    return render(request, 'import.html', {'oname': ProductType, 'opath': ProductType.lower()})
@login_required
def export_producttype(request, ProductType):
    model = globals()[ProductType]
    data = model.objects.all().values()
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename={ProductType.lower()}_export.xlsx'
    df.to_excel(response, index=False)
    return response


@login_required
def calculate_inpc(request):
    if request.method == 'POST':
        month = int(request.POST.get('month'))
        year = int(request.POST.get('year'))
        cart_id = request.POST.get('cart')

        # Convertir le mois et l'année en date
        selected_date = datetime(year, month, 1).date()

        # Récupérer le panier sélectionné
        cart = get_object_or_404(Cart, id=cart_id)

        # Récupérer les produits du panier
        cart_products = CartProducts.objects.filter(cart=cart)

        # Calculer l'INPC pour chaque mois de l'année en cours
        months = []
        inpc_values = []

        for m in range(1, 13):  # Boucle sur les 12 mois
            current_date = datetime(year, m, 1).date()
            total_cost = 0
            reference_cost = 0

            for cart_product in cart_products:
                # Récupérer le prix du produit pour le mois courant
                product_price = ProductPrice.objects.filter(
                    product=cart_product.product,
                    date_from__lte=current_date,
                    date_to__gte=current_date
                ).first()

                if product_price:
                    total_cost += product_price.value * cart_product.weight

                # Récupérer le prix du produit pour le mois de référence (mois précédent)
                reference_date = current_date - timedelta(days=30)  # Mois précédent
                reference_product_price = ProductPrice.objects.filter(
                    product=cart_product.product,
                    date_from__lte=reference_date,
                    date_to__gte=reference_date
                ).first()

                if reference_product_price:
                    reference_cost += reference_product_price.value * cart_product.weight

            # Calculer l'INPC pour le mois courant
            if reference_cost != 0:
                inpc = (total_cost / reference_cost) * 100
            else:
                inpc = 0

            # Ajouter les données pour le graphique
            months.append(f"{m}/{year}")
            inpc_values.append(inpc)

        # Récupérer l'INPC du mois sélectionné
        selected_inpc = inpc_values[month - 1]

        return render(request, 'inpc.html', {
            'inpc': selected_inpc,
            'month': month,
            'year': year,
            'cart': cart,
            'months': months,  # Liste des mois pour le graphique
            'inpc_values': inpc_values  # Liste des valeurs de l'INPC
        })

    # Récupérer tous les paniers pour la sélection
    carts = Cart.objects.all()
    return render(request, 'calcule_inpc.html', {'carts': carts})