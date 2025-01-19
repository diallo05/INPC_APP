from django.shortcuts import render
from django.db.models import Count  # Ajoutez cette ligne d'importation
from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import *
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    return render(request, 'home.html')


class productListView(ListView):
    model=Product
    template_name='product_list.html'
    context_object_name='product_list'

class productDetailView(DetailView):
    model=Product
    template_name='product_detail.html'
    context_object_name='product'

class productCreateView(CreateView):
    model=Product
    template_name='product_form.html'
    fields='__all__'
    success_url = reverse_lazy('product_list')

class productUpdateView(UpdateView):
    model=Product
    template_name='product_form.html'
    fields='__all__'

class productDeleteView(DeleteView):
    model=Product
    template_name='product_confirm_delete.html'
    success_url='/'
class pointVenteListView(ListView):
    model=PointOfSale
    template_name='pointvente_list.html'
    context_object_name='pointVente_list'

class ProductpriceListView(ListView):
    model=ProductPrice
    template_name='products.html'
    context_object_name='productprice_list'
class ProductpriceDetailView(DetailView):
    model=ProductPrice
    template_name='productprice_detail.html'
    context_object_name='productprice'

class ProductpriceCreateView(CreateView):
    model=ProductPrice
    template_name='productprice_form.html'
    fields='__all__'
    success_url = reverse_lazy('product_list')
class ProductpriceUpdateView(UpdateView):
    model=ProductPrice
    template_name='productprice_form.html'
    fields='__all__'

class ProductpriceDeleteView(DeleteView):
    model=ProductPrice
    template_name='productprice_confirm_delete.html'
    success_url='/'



class pointVenteDetailView(DetailView):
    model=PointOfSale
    template_name='pointVente_detail.html'
    context_object_name='pointVente'

class pointVenteCreateView(CreateView):
    model=PointOfSale
    template_name='pointvente_form.html'
    fields='__all__'
    success_url = reverse_lazy('pointVente_list')

class pointVenteUpdateView(UpdateView):
    model=PointOfSale
    template_name='pointVente_form.html'
    fields='__all__'

class pointVenteDeleteView(DeleteView):
    model=PointOfSale
    template_name='pointVente_confirm_delete.html'
    success_url='/'

class wilayaListView(ListView):
    model = Wilaya
    template_name = 'wilaya_map.html'
    context_object_name = 'wilaya_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Chemin vers le fichier GeoJSON des wilayas
        context['wilayas_geojson'] = 'static/geojson/wilayas.geojson'
        return context


class wilayaDetailView(DetailView): 
    model=Wilaya
    template_name='wilaya_detail.html'
    context_object_name='wilaya'

class wilayaCreateView(CreateView):
    model=Wilaya
    template_name='wilaya_form.html'
    fields='__all__'
    success_url = reverse_lazy('pointVente_list')

class wilayaUpdateView(UpdateView):
    model=Wilaya
    template_name='wilaya_form.html'
    fields='__all__'    

class wilayaDeleteView(DeleteView):
    model=Wilaya
    template_name='wilaya_confirm_delete.html'
    success_url='/'

class moughataaListView(ListView):
    model=Moughataa
    template_name='moughataa_list.html'
    context_object_name='moughataa_list'

class moughataaDetailView(DetailView):
    model=Moughataa
    template_name='moughataa_detail.html'
    context_object_name='moughataa'

class moughataaCreateView(CreateView):
    model=Moughataa
    template_name='moughataa_form.html'
    fields='__all__'
    success_url = reverse_lazy('pointVente_list')

class moughataaUpdateView(UpdateView):  
    model=Moughataa
    template_name='moughataa_form.html'
    fields='__all__'

class moughataaDeleteView(DeleteView):
    model=Moughataa
    template_name='moughataa_confirm_delete.html'
    success_url='/'

class communeListView(ListView):
    model=Commune
    template_name='commune_list.html'
    context_object_name='commune_list'  

class communeDetailView(DetailView):
    model=Commune
    template_name='commune_detail.html'
    context_object_name='commune'

class communeCreateView(CreateView):
    model=Commune
    template_name='commune_form.html'
    fields='__all__'
    success_url = reverse_lazy('commune_list')

class communeUpdateView(UpdateView):
    model=Commune
    template_name='commune_form.html'
    fields='__all__'

class communeDeleteView(DeleteView):
    model=Commune
    template_name='commune_confirm_delete.html'
    success_url='/'

class productTypeListView(ListView):
    model=ProductType
    template_name='producttype_list.html'
    context_object_name='productType_list'

class productTypeDetailView(DetailView):
    model=ProductType
    template_name='producttype_detail.html'
    context_object_name='productType'

class productTypeCreateView(CreateView):
    model=ProductType
    template_name='producttype_form.html'
    fields='__all__'
    success_url = reverse_lazy('productType_list')

class productTypeUpdateView(UpdateView):
    model=ProductType
    template_name='producttype_form.html'
    fields='__all__'

class productTypeDeleteView(DeleteView):
    model=ProductType
    template_name='producttype_confirm_delete.html'
    success_url='/'

class CartView(ListView):
    model=Cart
    template_name='cart_list.html'
    context_object_name='cart_list'

class CartDetailView(DetailView):
    model=Cart
    template_name='cart_detail.html'
    context_object_name='cart'

class CartCreateView(CreateView):
    model=Cart
    template_name='cart_form.html'
    fields='__all__'
    success_url = reverse_lazy('cart_list')

class CartUpdateView(UpdateView):        
    model=Cart
    template_name='cart_form.html'
    fields='__all__'

class CartDeleteView(DeleteView):    
    model=Cart
    template_name='cart_confirm_delete.html'
    success_url='/'



def import_wilaya_csv(request):
    if "GET" == request.method:
        return render(request, "csv_import.html", {'oname': "wilaya", 'opath': "wilayas"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:			
            fields = line.split(",")
            if len(fields) < 3 or not fields[0].isdigit():
                continue
            ob = Wilaya()
            ob.id = int(fields[0])
            ob.code = fields[1].strip()
            ob.name = fields[2].strip()
            object_list.append(ob)
        
        Wilaya.objects.bulk_create(object_list, ignore_conflicts=True)
        print(f"Successfully imported {len(object_list)} objects.")

    except Exception as e:
        print(f"Error! Unable to upload file: {e}")
        return HttpResponseRedirect(reverse("wilaya_import"))

    return HttpResponseRedirect(reverse("wilaya_list"))

def import_moughata_csv(request):
    if "GET" == request.method:
        return render(request, "csv_import.html", {'oname': "moughata", 'opath': "moughataas"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            fields = line.split(",")
            if len(fields) < 4 or not fields[0].isdigit():
                continue
            ob = Moughataa()
            ob.id = int(fields[0])
            ob.code = fields[1].strip()
            ob.label = fields[2].strip()
            
            # Trouver la wilaya correspondante
            try:
                wilaya = Wilaya.objects.get(name=fields[3].strip())
                ob.wilaya = wilaya
            except Wilaya.DoesNotExist:
                print(f"Wilaya not found: {fields[3].strip()}")
                continue
            
            object_list.append(ob)
        
        # Sauvegarder les objets dans la table Moughataa
        Moughataa.objects.bulk_create(object_list, ignore_conflicts=True)
        print(f"Successfully imported {len(object_list)} objects.")

    except Exception as e:
        print(f"Error! Unable to upload file: {e}")
        return HttpResponseRedirect(reverse("moughata_import"))

    return HttpResponseRedirect(reverse("wilaya_list"))


def dashboard(request):
    # Statistiques globales
    total_products = Product.objects.count()
    total_points_of_sales = PointOfSale.objects.count()
    total_moughataas = Moughataa.objects.count()
    total_communes = Commune.objects.count()

    # Données pour les graphiques
    # Répartition des types de produits
    product_types = Product.objects.annotate(product_count=Count('name'))
    product_type_labels = [ptype.name for ptype in product_types]
    product_type_data = [ptype.product_type for ptype in product_types]

    # Répartition des points de vente par type
    pointofsales_labels = PointOfSale.objects.values_list('type', flat=True).distinct()
    pointofsales_data = [PointOfSale.objects.filter(type=label).count() for label in pointofsales_labels]

    # Top 5 produits par prix (et génération des couleurs aléatoires pour chaque produit)
    top_5_products = ProductPrice.objects.order_by('-value')[:5]
    top_5_products_data = [
        {
            'name': ProductPrice.product,
            'price_data': [product.value * (1 + i * 0.05) for i in range(5)],  # Simulation de l'évolution des prix
            'color': f'#{i:06x}'  # Couleurs générées dynamiquement (hexadécimal)
        }
        for i, product in enumerate(top_5_products)
    ]



    # Rendu du template avec les données
    return render(request, 'dashboard.html', {
        'total_products': total_products,
        'total_points_of_sales': total_points_of_sales,
        'total_moughataas': total_moughataas,
        'total_communes': total_communes,
        'product_type_labels': product_type_labels,
        'product_type_data': product_type_data,
        'pointofsales_labels': pointofsales_labels,
        'pointofsales_data': pointofsales_data,
        'price_evolution_labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'top_5_products': top_5_products_data,

    })


def import_csv_commune(request):
    if "GET" == request.method:
        return render(request, "csv_import.html", {'oname': "commune", 'opath': "communes"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            fields = line.split(",")
            if len(fields) < 4 or not fields[0].isdigit():
                continue
            ob = Commune()
            ob.id = int(fields[0])
            ob.code = fields[1].strip()
            ob.name = fields[2].strip()
            try:
                moughataa = Moughataa.objects.get(label=fields[3].strip())
                ob.moughataa = moughataa
            except Moughataa.DoesNotExist:
                print(f"Moughataa not found: {fields[3].strip()}")
                continue
            object_list.append(ob)
        Commune.objects.bulk_create(object_list, ignore_conflicts=True)
        print(f"Successfully imported {len(object_list)} objects.")
    except Exception as e:
        print(f"Error! Unable to upload file: {e}")
        return HttpResponseRedirect(reverse("commune_import"))
    return HttpResponseRedirect(reverse("commune_list"))


