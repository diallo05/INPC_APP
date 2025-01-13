from django.urls import path
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", productListView.as_view(), name="product_list"),
    path("product/<int:pk>/", productDetailView.as_view(), name="product_detail"),
    path("product/new/", productCreateView.as_view(), name="product_new"),
    path("product/edit/<int:pk>/", productUpdateView.as_view(), name="product_edit"),
    path("product/delete/<int:pk>/", productDeleteView.as_view(), name="product_delete"),
    path("pointVente/list", pointVenteListView.as_view(), name="pointVente_list"),
    path("pointVente/<int:pk>/", pointVenteDetailView.as_view(), name="pointVente_detail"),
    path("pointVente/new/", pointVenteCreateView.as_view(), name="pointVente_new"),
    path("pointVente/edit/<int:pk>/", pointVenteUpdateView.as_view(), name="pointVente_edit"),
    path("pointVente/delete/<int:pk>/", pointVenteDeleteView.as_view(), name="pointVente_delete"),
    path("count_categories/", count_categories, name="count_categories"),
    path("count_communes/", count_communes, name="count_communes"),
    path("count_total_pointvente/", count_total_pointvente, name="count_total_pointvente"),
]
