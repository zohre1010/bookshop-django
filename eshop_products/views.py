from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category
from django.contrib import messages
from utils import IsAdminUserMixin
from eshop_slider.models import Slider
from eshop_order.forms import CartAddForm
from django.views.generic import ListView
import itertools


# class ListView(ListView):
# 	paginate_by = 1
# 	def get(self, request, category_slug=None):
# 		products = Product.objects.filter(available=True)
# 		categories = Category.objects.filter(is_sub=False)
# 		if category_slug:
# 			category = Category.objects.get(slug=category_slug)
# 			products = products.filter(category=category)
# 		return render(request, 'eshop_products/list.html', {'products':products, 'categories':categories})
	
def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class ListView(ListView):
    template_name = 'eshop_products/list.html'
    paginate_by = 1
   
    def get_context_data(self, *args , object_list = None ,category_slug=None, **kwargs):
        
        latest_products = Product.objects.order_by('-id').filter(available=True)[:3]
        products = Product.objects.filter(available=True)
        categories=Category.objects.filter(is_sub=False)
        if category_slug:
           category=Category.objects.filter(slug=category_slug)
           products=products.filter(category=category)
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context['categories'] = categories
        context['products'] = products
        # context['most_visit'] = my_grouper(1, most_visit_news)
        context['latest_products'] = my_grouper(3, latest_products)
       
        return context  
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)
    
    def get_queryset(self):
        return Product.objects.filter(available=True)
    
class ProductDetailView(View):
	def get(self, request, slug):
		category_parent=Category.objects.filter(is_sub=False)
		product = get_object_or_404(Product, slug=slug)
		form = CartAddForm()
		return render(request, 'eshop_products/detail.html', {'product':product, 'form':form,'category_parent':category_parent})
