from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Produit, PointVente, Panier, ProduitPanier, ProduitPointVente, Indice

# Create your views here.

class productListView(ListView):
    model=Produit
    template_name='test.html'
    context_object_name='product_list'

class productDetailView(DetailView):
    model=Produit
    template_name='product_detail.html'
    context_object_name='product'

class productCreateView(CreateView):
    model=Produit
    template_name='product_form.html'
    fields='__all__'
    success_url = reverse_lazy('product_list')

class productUpdateView(UpdateView):
    model=Produit
    template_name='product_form.html'
    fields='__all__'

class productDeleteView(DeleteView):
    model=Produit
    template_name='product_confirm_delete.html'
    success_url='/'
class pointVenteListView(ListView):
    model=PointVente
    template_name='pointvente_list.html'
    context_object_name='pointVente_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_communes'] = count_communes()  # Calcul du nombre de communes
        context['count_categories'] = count_categories()  # Calcul du nombre de catégories
        context['count_total_pointvente'] = count_total_pointvente()  # Total des points de vente
        return context

class pointVenteDetailView(DetailView):
    model=PointVente
    template_name='pointVente_detail.html'
    context_object_name='pointVente'

class pointVenteCreateView(CreateView):
    model=PointVente
    template_name='pointVente_form.html'
    fields='__all__'
    success_url = reverse_lazy('pointVente_list')

class pointVenteUpdateView(UpdateView):
    model=PointVente
    template_name='pointVente_form.html'
    fields='__all__'

class pointVenteDeleteView(DeleteView):
    model=PointVente
    template_name='pointVente_confirm_delete.html'
    success_url='/'

# Fonction pour compter le nombre de catégories distinctes
def count_categories():
    return PointVente.objects.values('categorie').distinct().count()

# Fonction pour compter le nombre de communes distinctes
def count_communes():
    return PointVente.objects.values('commune').distinct().count()

# Fonction pour compter le nombre total de PointVente
def count_total_pointvente():
    return PointVente.objects.count()