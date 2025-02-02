from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.db.models import Avg, Count # type: ignore
from django.contrib import messages # type: ignore
from django.db.models import Count  # type: ignore # Ajoutez cette ligne d'importation
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView # type: ignore
from django.urls import reverse_lazy, reverse # type: ignore
from .models import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from django.conf import settings
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
import matplotlib.pyplot as plt
from django.http import HttpResponseRedirect, HttpResponse
import pandas as pd
import io
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from datetime import datetime, timedelta
from django.conf import settings
from .forms import ExcelImportForm
from collections import Counter, defaultdict
from django.views.generic.edit import FormView
from django.utils import timezone
from django.contrib.auth import logout
import numpy as np 
import json
# Create your views here.

def custom_logout(request):
    logout(request)
    return redirect('home')

class productListView(LoginRequiredMixin,ListView):
    model=Product
    template_name='product_list.html'
    context_object_name='product_list'

class productDetailView(LoginRequiredMixin,DetailView):
    model=Product
    template_name='product_details.html'
    context_object_name='product'

class productCreateView(LoginRequiredMixin,CreateView):
    model=Product
    template_name='product_form.html'
    fields='__all__'
    success_url = reverse_lazy('product_list')

class productUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = '__all__'
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
    template_name='productprice_details.html'
    context_object_name='productprice'

class ProductpriceCreateView(LoginRequiredMixin,CreateView):
    model=ProductPrice
    template_name='productprice_form.html'
    fields='__all__'
    success_url = reverse_lazy('productprice_list')
class ProductpriceUpdateView(LoginRequiredMixin,UpdateView):
    model=ProductPrice
    template_name='productprice_form.html'
    fields='__all__'
    success_url = reverse_lazy('productprice_list')

class ProductpriceDeleteView(LoginRequiredMixin,DeleteView):
    model=ProductPrice
    template_name='productprice_confirm_delete.html'
    success_url='productprice_list'



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
    success_url = reverse_lazy('pointVente_list')

class pointVenteDeleteView(LoginRequiredMixin,DeleteView):
    model=PointOfSale
    template_name='pointVente_confirm_delete.html'
    success_url='pointVente_list'

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
    success_url = reverse_lazy('wilaya_list')

class wilayaUpdateView(LoginRequiredMixin,UpdateView):
    model=Wilaya
    template_name='wilaya_form.html'
    fields='__all__'
    success_url = reverse_lazy('wilaya_list')

class wilayaDeleteView(LoginRequiredMixin,DeleteView):
    model=Wilaya
    template_name='wilaya_confirm_delete.html'
    success_url='wilaya_list'

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
    success_url = reverse_lazy('moughataa_list')

class moughataaUpdateView(LoginRequiredMixin,UpdateView):  
    model=Moughataa
    template_name='moughataa_form.html'
    fields='__all__'
    success_url = reverse_lazy('moughataa_list')

class moughataaDeleteView(LoginRequiredMixin,DeleteView):
    model=Moughataa
    template_name='moughataa_confirm_delete.html'
    success_url='moughataa_list'

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
    success_url = reverse_lazy('commune_list')

class communeDeleteView(LoginRequiredMixin,DeleteView):
    model=Commune
    template_name='commune_confirm_delete.html'
    success_url='commune_list'

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
    success_url = reverse_lazy('productType_list')

class productTypeDeleteView(LoginRequiredMixin,DeleteView):
    model=ProductType
    template_name='producttype_confirm_delete.html'
    success_url='productType_list'

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
    success_url = reverse_lazy('cart_list')

class CartDeleteView(LoginRequiredMixin,DeleteView):    
    model=Cart
    template_name='cart_confirm_delete.html'
    success_url='cart_list'

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
    success_url = reverse_lazy('cartproduct_list')

class CartProductDeleteView(LoginRequiredMixin,DeleteView):    
    model=CartProducts
    template_name='cart_confirm_delete.html'
    success_url='cartproduct_list'



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
    # Récupération des paramètres de filtrage depuis l'URL
    selected_year = request.GET.get('year')
    selected_moughataa = request.GET.get('moughataa')

    # Obtenir toutes les années disponibles dans les données
    available_years = ProductPrice.objects.dates('date_from', 'year').distinct()
    available_years = [year.year for year in available_years]

    # Obtenir toutes les Moughataas disponibles
    available_moughataas = Moughataa.objects.all()

    # Filtrage des prix des produits par année
    if selected_year:
        product_prices = ProductPrice.objects.filter(date_from__year=selected_year)
    else:
        product_prices = ProductPrice.objects.all()

    # Comptage des entités principales
    commune_count = Commune.objects.count()
    wilaya_count = Wilaya.objects.count()
    moughataa_count = Moughataa.objects.count()
    product_count = Product.objects.count()

    # Comptage des produits par type
    product_types = Product.objects.values('product_type__label')
    product_type_count = Counter([ptype['product_type__label'] for ptype in product_types])
    product_type_labels = list(product_type_count.keys())
    product_type_values = list(product_type_count.values())

    # Filtrage des points de vente par Moughataa sélectionnée
    if selected_moughataa:
        point_of_sale_data = PointOfSale.objects.filter(commune__moughataa__id=selected_moughataa).values('commune__name')
    else:
        point_of_sale_data = PointOfSale.objects.values('commune__name')

    point_of_sale_count = Counter([pos['commune__name'] for pos in point_of_sale_data])
    point_of_sale_labels = list(point_of_sale_count.keys())
    point_of_sale_values = list(point_of_sale_count.values())

    # Récupération des prix de produits par date
    price_data = defaultdict(lambda: defaultdict(list))
    for price in product_prices:
        price_data[price.product.id]['dates'].append(price.date_from)
        price_data[price.product.id]['values'].append(price.value)

    # Préparer les données pour le graphique d'évolution des prix
    line_chart_labels = []
    line_chart_datasets = []
    for product_id, data in price_data.items():
        sorted_dates = sorted(data['dates'])
        sorted_values = [data['values'][data['dates'].index(date)] for date in sorted_dates]
        product_name = Product.objects.get(id=product_id).name
        if not line_chart_labels:
            line_chart_labels = [date.strftime('%Y-%m-%d') for date in sorted_dates]
        line_chart_datasets.append({
            'label': product_name,
            'data': sorted_values,
            'fill': False,
            'borderColor': 'rgba(75, 192, 192, 1)',
            'tension': 0.1
        })

    # Calcul de l'IPC pour l'année sélectionnée
    ipc_data = product_prices.values('date_from').annotate(avg_price=Avg('value')).order_by('date_from')
    ipc_labels = [entry['date_from'].strftime('%Y-%m-%d') for entry in ipc_data]
    ipc_values = [entry['avg_price'] for entry in ipc_data]

    # Préparer les données pour le graphique IPC
    ipc_chart_dataset = [{
        'label': 'Indice des Prix à la Consommation',
        'data': ipc_values,
        'fill': False,
        'borderColor': 'rgba(255, 99, 132, 1)',
        'tension': 0.1
    }]

    # Récupérer les points de vente avec coordonnées GPS
    point_of_sales = PointOfSale.objects.filter(gps_lat__isnull=False, gps_lon__isnull=False).values(
        'id', 'code', 'gps_lat', 'gps_lon', 'commune__name')
    point_of_sales_json = json.dumps(list(point_of_sales))

    # Générer un résumé des statistiques IPC
    ipc_summary = {
        'date_debut': ipc_labels[0] if ipc_labels else 'N/A',
        'date_fin': ipc_labels[-1] if ipc_labels else 'N/A',
        'ipc_moyen': round(sum(ipc_values) / len(ipc_values), 2) if ipc_values else 'N/A',
        'ipc_max': max(ipc_values) if ipc_values else 'N/A',
        'ipc_min': min(ipc_values) if ipc_values else 'N/A',
    }

    # Passer les données au template
    context = {
        'commune_count': commune_count,
        'wilaya_count': wilaya_count,
        'moughataa_count': moughataa_count,
        'product_count': product_count,
        'product_type_labels': product_type_labels,
        'product_type_values': product_type_values,
        'point_of_sale_labels': json.dumps(point_of_sale_labels),
        'point_of_sale_values': json.dumps(point_of_sale_values),
        'line_chart_labels': json.dumps(line_chart_labels),
        'line_chart_datasets': json.dumps(line_chart_datasets),
        'ipc_labels': json.dumps(ipc_labels),
        'ipc_chart_dataset': json.dumps(ipc_chart_dataset),
        'ipc_summary': ipc_summary,
        'available_years': available_years,
        'selected_year': selected_year,
        'available_moughataas': available_moughataas,
        'selected_moughataa': selected_moughataa,
        'point_of_sales_json': point_of_sales_json,
    }

    return render(request, 'dashboard.html', context)

 

@login_required
def generate_report(request):
    # Récupérer les données statistiques
    commune_count = Commune.objects.count()
    wilaya_count = Wilaya.objects.count()
    moughataa_count = Moughataa.objects.count()
    product_count = Product.objects.count()

    # Récupération des prix de produits par date
    product_prices = ProductPrice.objects.all()
    price_data = defaultdict(lambda: defaultdict(list))
    for price in product_prices:
        price_data[price.product.id]['dates'].append(price.date_from)
        price_data[price.product.id]['values'].append(price.value)

    # Récupérer les points de vente avec coordonnées GPS
    point_of_sales = PointOfSale.objects.filter(gps_lat__isnull=False, gps_lon__isnull=False).values(
        'id', 'code', 'gps_lat', 'gps_lon', 'commune__name')

    # Calcul de l'Indice des Prix à la Consommation (IPC)
    ipc_data = ProductPrice.objects.values('date_from').annotate(avg_price=Avg('value')).order_by('date_from')
    ipc_labels = [entry['date_from'].strftime('%Y-%m-%d') for entry in ipc_data]
    ipc_values = [entry['avg_price'] for entry in ipc_data]

    # Préparer la réponse PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport_ipc.pdf"'

    # Créer un objet PDF avec ReportLab
    pdf = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Ajouter la page de garde
    cover_path = os.path.join(settings.BASE_DIR, "staticfiles", "page_garde.png")
    if os.path.exists(cover_path):
        # Ajouter l'image de la page de garde
        cover_image = Image(cover_path, width=400, height=500)
        elements.append(cover_image)
        elements.append(PageBreak())
    else:
        elements.append(Paragraph("Page de garde non trouvée", styles['Title']))

    # Ajouter le logo dans l'en-tête
    logo_path = os.path.join(os.path.dirname(__file__), "static", "logo.png")
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=100, height=50)
        elements.append(logo)
    else:
        elements.append(Paragraph("Logo non trouvé", styles['Normal']))

    # Titre du rapport
    elements.append(Paragraph("Rapport sur l'Indice des Prix à la Consommation", styles['Title']))
    elements.append(Paragraph(f"Date : {datetime.now().strftime('%Y-%m-%d')}", styles['Normal']))

    # Tableau des statistiques générales
    data = [
        ["Statistique", "Valeur"],
        ["Nombre de Communes", commune_count],
        ["Nombre de Wilayas", wilaya_count],
        ["Nombre de Moughataas", moughataa_count],
        ["Nombre de Produits", product_count],
    ]
    
    table = Table(data, colWidths=[200, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(table)

    # Graphique d'évolution des prix des produits
    plt.figure(figsize=(10, 6))
    for product_id, data in price_data.items():
        product_name = Product.objects.get(id=product_id).name
        sorted_dates = sorted(data['dates'])
        sorted_values = [data['values'][data['dates'].index(date)] for date in sorted_dates]
        plt.plot(sorted_dates, sorted_values, label=product_name)

    plt.title("Évolution des Prix des Produits")
    plt.xlabel("Date")
    plt.ylabel("Prix")
    plt.legend()
    plt.grid(True)

    # Sauvegarder le graphique en tant qu'image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Ajouter l'image au PDF
    elements.append(Paragraph("Évolution des Prix des Produits", styles['Heading2']))
    elements.append(Image(buf, width=500, height=300))

    # Commentaire pour le graphique d'évolution des prix
    elements.append(Paragraph("Commentaire : Ce graphique montre l'évolution des prix des produits sur une période donnée.", styles['Normal']))

    # Graphique de l'IPC
    plt.figure(figsize=(10, 6))
    plt.plot(ipc_labels, ipc_values, marker='o', color='r', label='IPC')
    plt.title("Indice des Prix à la Consommation (IPC)")
    plt.xlabel("Date")
    plt.ylabel("IPC")
    plt.legend()
    plt.grid(True)

    # Sauvegarder le graphique en tant qu'image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Ajouter l'image au PDF
    elements.append(Paragraph("Indice des Prix à la Consommation (IPC)", styles['Heading2']))
    elements.append(Image(buf, width=500, height=300))

    # Commentaire pour le graphique IPC
    elements.append(Paragraph("Commentaire : Ce graphique montre l'évolution de l'Indice des Prix à la Consommation (IPC) sur une période donnée.", styles['Normal']))

    # Tableau 1 : Evolution de l’Indice National des Prix à la Consommation en novembre 2024
    elements.append(Paragraph("Tableau 1 : Evolution de l’Indice National des Prix à la Consommation en novembre 2024", styles['Heading2']))
    ipc_table_data = [
        ["Date", "IPC"],
        *[[label, value] for label, value in zip(ipc_labels, ipc_values)]
    ]
    ipc_table = Table(ipc_table_data, colWidths=[200, 200])
    ipc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(ipc_table)

    # Tableau 2 : Statistique par produits (évolution des prix)
    elements.append(Paragraph("Tableau 2 : Statistique par produits (évolution des prix)", styles['Heading2']))
    product_stats_data = [
        ["Produit", "Prix Moyen", "Variation"],
        *[[product.name, np.mean(price_data[product.id]['values']), np.std(price_data[product.id]['values'])] for product in Product.objects.all()]
    ]
    product_stats_table = Table(product_stats_data, colWidths=[200, 100, 100])
    product_stats_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(product_stats_table)

    # Tableau 3 : Evolution de l’indice par fonctions en novembre 2024
    elements.append(Paragraph("Tableau 3 : Evolution de l’indice par fonctions en novembre 2024", styles['Heading2']))
    # Ici, vous pouvez ajouter des données spécifiques pour l'évolution par fonctions
    function_stats_data = [
        ["Fonction", "IPC"],
        ["Alimentation", 120.5],
        ["Logement", 110.3],
        ["Transport", 105.7],
        # Ajoutez d'autres fonctions et leurs IPC ici
    ]
    function_stats_table = Table(function_stats_data, colWidths=[200, 200])
    function_stats_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(function_stats_table)

    # Graphique 3 : Evolutions mensuelles des indices en novembre 2024 selon les point of sales
    elements.append(Paragraph("Graphique 3 : Evolutions mensuelles des indices en novembre 2024 selon les point of sales", styles['Heading2']))
    # Ici, vous pouvez générer un graphique basé sur les données des points de vente
    plt.figure(figsize=(10, 6))
    for pos in point_of_sales:
        pos_prices = ProductPrice.objects.filter(point_of_sale=pos['id']).values('date_from').annotate(avg_price=Avg('value')).order_by('date_from')
        pos_labels = [entry['date_from'].strftime('%Y-%m-%d') for entry in pos_prices]
        pos_values = [entry['avg_price'] for entry in pos_prices]
        plt.plot(pos_labels, pos_values, label=pos['commune__name'])

    plt.title("Évolution des Prix par Point de Vente")
    plt.xlabel("Date")
    plt.ylabel("Prix")
    plt.legend()
    plt.grid(True)

    # Sauvegarder le graphique en tant qu'image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Ajouter l'image au PDF
    elements.append(Image(buf, width=500, height=300))

    # Générer le PDF
    pdf.build(elements)
    
    return response



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