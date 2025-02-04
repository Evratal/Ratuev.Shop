from django.urls import path
from pythonProject.catalog.apps import CatalogConfig
from pythonProject.catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name = 'home'),
    path('contacts/', contacts, name = 'contacts')
]
