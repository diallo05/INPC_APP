from django.urls import path
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("product/list/", productListView.as_view(), name="product_list"),
    path("product/<int:pk>/", productDetailView.as_view(), name="product_detail"),
    path("product/new/", productCreateView.as_view(), name="product_new"),
    path("product/edit/<int:pk>/", productUpdateView.as_view(), name="product_edit"),
    path("product/delete/<int:pk>/", productDeleteView.as_view(), name="product_delete"),
    path("productprice/list", ProductpriceListView.as_view(), name="productprice_list"),
    path("productprice/<int:pk>/", ProductpriceDetailView.as_view(), name="productprice_detail"),
    path("productprice/new/", ProductpriceCreateView.as_view(), name="productprice_new"),
    path("productprice/edit/<int:pk>/", ProductpriceUpdateView.as_view(), name="productprice_edit"),
    path("productprice/delete/<int:pk>/", ProductpriceDeleteView.as_view(), name="productprice_delete"),
    path("pointVente/list", pointVenteListView.as_view(), name="pointVente_list"),
    path("pointVente/<int:pk>/", pointVenteDetailView.as_view(), name="pointVente_detail"),
    path("pointVente/new/", pointVenteCreateView.as_view(), name="pointVente_new"),
    path("pointVente/edit/<int:pk>/", pointVenteUpdateView.as_view(), name="pointVente_edit"),
    path("pointVente/delete/<int:pk>/", pointVenteDeleteView.as_view(), name="pointVente_delete"),
    path("productType/list", productTypeListView.as_view(), name="productType_list"),
    path("productType/<int:pk>/", productTypeDetailView.as_view(), name="productType_detail"),
    path("productType/new/", productTypeCreateView.as_view(), name="productType_new"),
    path("productType/edit/<int:pk>/", productTypeUpdateView.as_view(), name="productType_edit"),
    path("productType/delete/<int:pk>/", productTypeDeleteView.as_view(), name="productType_delete"),
    path("wilaya/list", wilayaListView.as_view(), name="wilaya_list"),
    path("wilaya/<int:pk>/", wilayaDetailView.as_view(), name="wilaya_detail"),
    path("wilaya/new/", wilayaCreateView.as_view(), name="wilaya_new"),
    path("wilaya/edit/<int:pk>/", wilayaUpdateView.as_view(), name="wilaya_edit"),
    path("wilaya/delete/<int:pk>/", wilayaDeleteView.as_view(), name="wilaya_delete"),
    path("moughataa/list", moughataaListView.as_view(), name="moughataa_list"),
    path("moughataa/<int:pk>/", moughataaDetailView.as_view(), name="moughataa_detail"),
    path("moughataa/new/", moughataaCreateView.as_view(), name="moughataa_new"),
    path("moughataa/edit/<int:pk>/", moughataaUpdateView.as_view(), name="moughataa_edit"),
    path("moughataa/delete/<int:pk>/", moughataaDeleteView.as_view(), name="moughataa_delete"),
    path("commune/list", communeListView.as_view(), name="commune_list"),
    path("commune/<int:pk>/", communeDetailView.as_view(), name="commune_detail"),
    path("commune/new/", communeCreateView.as_view(), name="commune_new"),
    path("commune/edit/<int:pk>/", communeUpdateView.as_view(), name="commune_edit"),
    path("commune/delete/<int:pk>/", communeDeleteView.as_view(), name="commune_delete"),
    path("cart/list", CartView.as_view(), name="cart_list"),
    path("cart/<int:pk>/", CartDetailView.as_view(), name="cart_detail"),
    path("cart/new/", CartCreateView.as_view(), name="cart_new"),
    path("cart/edit/<int:pk>/", CartUpdateView.as_view(), name="cart_edit"),
    path("cart/delete/<int:pk>/", CartDeleteView.as_view(), name="cart_delete"),
    path('import/wilayas', import_wilaya_csv, name='wilaya_import'),
    path('import/moughataas', import_moughata_csv, name='moughata_import'),
    path("dashboard/", dashboard, name="dashboard"),
    path('import/communes', import_csv_commune, name='commune_import'),
]
