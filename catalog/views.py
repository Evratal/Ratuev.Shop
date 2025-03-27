from itertools import product

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation.trans_real import catalog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product



class HomeView(TemplateView):
    template_name = 'catalog/home.html'

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView,LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user==self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.can_delete_any_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView,LoginRequiredMixin, UserPassesTestMixin):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def test_func(self):
        product = self.get_object()
        # Проверяем, что пользователь — владелец ИЛИ имеет право can_delete_any_product
        return (
                product.owner == self.request.user
                or self.request.user.has_perm("catalog.can_delete_any_product")
        )

@permission_required("catalog.can_unpublish_product")
def unpublish_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.publish_status = False
    product.save()
    return redirect("product_list")