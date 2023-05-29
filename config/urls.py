"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from config import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('products/',include('eshop_products.urls', namespace='eshop_products')),
    path('',include('eshop_accounts.urls', namespace='eshop_accounts')),
    path('blog/',include('eshop_blog.urls', namespace='eshop_blog')),
    path('orders/',include('eshop_order.urls', namespace='eshop_order')),
    path('header',views.Header.as_view(), name='header'),
    path('menu/', views.Header.as_view(), name='menu'),
    path('footer',views.footer, name='footer'),
    path('', include('eshop_contact.urls',namespace='eshop_contact')),
    path('about-us/', views.about_page),
    path('admin/', admin.site.urls),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),  
]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)