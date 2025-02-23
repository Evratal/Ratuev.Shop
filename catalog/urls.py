from django.urls import path
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name = 'catalog'),
    path('contacts/', contacts, name = 'contacts'),
    path('catalog/product_list/', ProductListView.as_view(), name = "product_list"),
    path('catalog/product/<int:pk>/',ProductDetailView.as_view(), name = "product_detail"),
    path('catalog/create',ProductCreateView.as_view(), name = "product_create"),
    path('catalog/<int:pk>/update/',ProductUpdateView.as_view(), name = "product_update"),
    path('catalog/<int:pk>/delet/',ProductDeleteView.as_view(), name = "product_delete")

]
