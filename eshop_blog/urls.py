
from django.urls import path
from . import views
app_name = 'blog_app'

urlpatterns = [
    
	path('list/', views.BlogListView.as_view(), name='blog_list'),
	path('category/<slug:category_slug>/', views.BlogListView.as_view(), name='category_filter'),
	path('<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    
]