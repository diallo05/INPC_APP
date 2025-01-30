from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.db.models import Avg, Count # type: ignore
from django.contrib import messages # type: ignore
from django.db.models import Count  # type: ignore # Ajoutez cette ligne d'importation
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView # type: ignore
from django.urls import reverse_lazy, reverse # type: ignore
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from .forms import ExcelImportForm
from django.views.generic.edit import FormView


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


@login_required
def dashboard(request):
    # Statistiques des produits
    product_stats = Product.objects.annotate(num_prices=Count('productprice')).values('name', 'num_prices')
    avg_price = ProductPrice.objects.aggregate(avg_price=Avg('value'))['avg_price']

    # Statistiques des points de vente
    point_of_sale_stats = PointOfSale.objects.values('commune__name').annotate(num_points=Count('id'))

    # Données pour l'INPC
    carts = Cart.objects.all()
    inpc_data = []
    for cart in carts:
        cart_products = CartProducts.objects.filter(cart=cart)
        total_cost = sum(cp.weight * cp.product.productprice_set.first().value for cp in cart_products if cp.product.productprice_set.exists())
        inpc_data.append({
            'cart_name': cart.name,
            'total_cost': total_cost
        })

    # Données pour les graphiques
    product_prices = ProductPrice.objects.values('product__name', 'value', 'date_from')

    context = {
        'product_stats': product_stats,
        'avg_price': avg_price,
        'point_of_sale_stats': point_of_sale_stats,
        'inpc_data': inpc_data,
        'product_prices': product_prices,
    }
    return render(request, 'dashboard.html', context)


class ExcelImportView(LoginRequiredMixin, FormView):
    template_name = 'import.html'
    form_class = ExcelImportForm
    success_url = '/import/'

    # Configuration des colonnes attendues pour chaque modèle
    def get_expected_columns(self, model_type):
        column_map = {
            'product_type': ['code', 'label', 'description'],
            'product': ['code', 'name', 'description', 'unit_measure', 'product_type'],
            'wilaya': ['code', 'name'],
            'moughataa': ['code', 'label', 'wilaya'],
            'commune': ['code', 'name', 'moughataa'],
            'point_of_sale': ['code', 'type', 'gps_lat', 'gps_lon', 'commune'],
            'product_price': ['value', 'date_from', 'date_to', 'product', 'point_of_sale'],
            'cart': ['code', 'name', 'description'],
            'cart_product': ['cart', 'product', 'weight', 'date_from', 'date_to']
        }
        return column_map.get(model_type, [])

    def form_valid(self, form):
        operation = form.cleaned_data['operation']
        model_type = form.cleaned_data['model_type']
        uploaded_file = form.cleaned_data.get('file')

        try:
            if operation == 'import':
                return self.handle_import(model_type, uploaded_file)
            elif operation == 'export':
                return self.handle_export(model_type)
        except Exception as e:
            messages.error(self.request, f'Erreur : {str(e)}')
        
        return super().form_valid(form)

    # Gestion des imports
    def handle_import(self, model_type, uploaded_file):
        import_methods = {
            'product_type': self.import_product_types,
            'product': self.import_products,
            'wilaya': self.import_wilayas,
            'moughataa': self.import_moughataas,
            'commune': self.import_communes,
            'point_of_sale': self.import_points_of_sale,
            'product_price': self.import_product_prices,
            'cart': self.import_carts,
            'cart_product': self.import_cart_products
        }
        
        df = pd.read_excel(uploaded_file)
        missing_cols = set(self.get_expected_columns(model_type)) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Colonnes manquantes: {', '.join(missing_cols)}")
        
        result = import_methods[model_type](df)
        if result['errors']:
            messages.warning(self.request, f"Erreurs détectées : {len(result['errors'])}")
        else:
            messages.success(self.request, 'Importation réussie !')
        
        return redirect(self.success_url)

    # Gestion des exports
    def handle_export(self, model_type):
        export_methods = {
            'product_type': self.export_product_types,
            'product': self.export_products,
            'wilaya': self.export_wilayas,
            'moughataa': self.export_moughataas,
            'commune': self.export_communes,
            'point_of_sale': self.export_points_of_sale,
            'product_price': self.export_product_prices,
            'cart': self.export_carts,
            'cart_product': self.export_cart_products
        }
        
        df = export_methods[model_type]()
        buffer = io.BytesIO()
        df.to_excel(buffer, index=False, engine='openpyxl')
        buffer.seek(0)
        
        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{model_type}_export.xlsx"'
        return response

    # Méthodes d'importation pour chaque modèle
    def import_product_types(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                ProductType.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'label': row['label'],
                        'description': row.get('description', '')
                    }
                )
            except Exception as e:
                errors.append(f"ProductType {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_products(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                product_type = ProductType.objects.get(code=row['product_type'])
                Product.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'name': row['name'],
                        'description': row.get('description', ''),
                        'unit_measure': row['unit_measure'],
                        'product_type': product_type
                    }
                )
            except Exception as e:
                errors.append(f"Product {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_wilayas(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                Wilaya.objects.update_or_create(
                    code=row['code'],
                    defaults={'name': row['name']}
                )
            except Exception as e:
                errors.append(f"Wilaya {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_moughataas(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                wilaya = Wilaya.objects.get(code=row['wilaya'])
                Moughataa.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'label': row['label'],
                        'wilaya': wilaya
                    }
                )
            except Exception as e:
                errors.append(f"Moughataa {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_communes(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                moughataa = Moughataa.objects.get(code=row['moughataa'])
                Commune.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'name': row['name'],
                        'moughataa': moughataa
                    }
                )
            except Exception as e:
                errors.append(f"Commune {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_points_of_sale(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                commune = Commune.objects.get(code=row['commune'])
                PointOfSale.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'type': row['type'],
                        'gps_lat': row.get('gps_lat'),
                        'gps_lon': row.get('gps_lon'),
                        'commune': commune
                    }
                )
            except Exception as e:
                errors.append(f"POS {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_product_prices(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                product = Product.objects.get(code=row['product'])
                pos = PointOfSale.objects.get(code=row['point_of_sale'])
                ProductPrice.objects.update_or_create(
                    product=product,
                    point_of_sale=pos,
                    date_from=row['date_from'],
                    defaults={
                        'value': row['value'],
                        'date_to': row.get('date_to')
                    }
                )
            except Exception as e:
                errors.append(f"Price {row['product']}-{row['point_of_sale']}: {str(e)}")
        return {'errors': errors}

    def import_carts(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                Cart.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'name': row['name'],
                        'description': row.get('description', '')
                    }
                )
            except Exception as e:
                errors.append(f"Cart {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_cart_products(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                cart = Cart.objects.get(code=row['cart'])
                product = Product.objects.get(code=row['product'])
                CartProducts.objects.update_or_create(
                    cart=cart,
                    product=product,
                    date_from=row['date_from'],
                    defaults={
                        'weight': row['weight'],
                        'date_to': row.get('date_to')
                    }
                )
            except Exception as e:
                errors.append(f"CartProduct {row['cart']}-{row['product']}: {str(e)}")
        return {'errors': errors}

    # Méthodes d'exportation pour chaque modèle
    def export_product_types(self):
        return pd.DataFrame.from_records(
            ProductType.objects.all().values('code', 'label', 'description')
        )

    def export_products(self):
        return pd.DataFrame.from_records(
            Product.objects.all().values(
                'code', 'name', 'description', 
                'unit_measure', 'product_type__code'
            )
        )

    def export_wilayas(self):
        return pd.DataFrame.from_records(
            Wilaya.objects.all().values('code', 'name')
        )

    def export_moughataas(self):
        return pd.DataFrame.from_records(
            Moughataa.objects.select_related('wilaya').values(
                'code', 'label', 'wilaya__code'
            )
        )

    def export_communes(self):
        return pd.DataFrame.from_records(
            Commune.objects.select_related('moughataa').values(
                'code', 'name', 'moughataa__code'
            )
        )

    def export_points_of_sale(self):
        return pd.DataFrame.from_records(
            PointOfSale.objects.select_related('commune').values(
                'code', 'type', 'gps_lat', 'gps_lon', 'commune__code'
            )
        )

    def export_product_prices(self):
        return pd.DataFrame.from_records(
            ProductPrice.objects.select_related('product', 'point_of_sale').values(
                'product__code',
                'point_of_sale__code',
                'value',
                'date_from',
                'date_to'
            )
        )

    def export_carts(self):
        return pd.DataFrame.from_records(
            Cart.objects.all().values('code', 'name', 'description')
        )

    def export_cart_products(self):
        return pd.DataFrame.from_records(
            CartProducts.objects.select_related('cart', 'product').values(
                'cart__code',
                'product__code',
                'weight',
                'date_from',
                'date_to'
            )
        )