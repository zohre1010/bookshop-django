from django.shortcuts import render
from django.views import View

from eshop_slider.models import Slider
from eshop_products.models import Product, Category

import itertools
from eshop_settings.models import SiteSetting
from eshop_blog.models import Blog


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class HomeView(View):
	def get(self, request):
		sliders = Slider.objects.all()
		blogs=Blog.objects.order_by('-id').all()[:3]
		most_visit_products = Product.objects.order_by('-visit_count').all()[:6]
		latest_products = Product.objects.order_by('-id').all()[:3]
		
		context = {
        'sliders': sliders,
        'most_visit': my_grouper(2, most_visit_products),
        'latest_products': my_grouper(1, latest_products),
		
		 'blogs':my_grouper(1, blogs),
    }   

		return render(request, 'home_page.html', context)
class Header(View):
	def get(self, request):
		# menus = Menu.objects.filter(is_sub=False)
		site_setting = SiteSetting.objects.first()
		category_parent=Category.objects.filter(is_sub=False)
		context = {
        'setting': site_setting,
		'category_parent':category_parent
		}

			
		return render(request, 'shared/Header.html', context)

# footer code behind
def footer(request, *args, **kwargs):
	site_setting = SiteSetting.objects.first()
	category_parent=Category.objects.filter(is_sub=False)
	context = {
        'setting': site_setting,
		'category_parent':category_parent	
    }
	return render(request, 'shared/Footer.html',context)



def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }

    return render(request, 'about_page.html', context)
