from django.shortcuts import render
from django.views import View
from .models import Blog,Category
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView


# Create your views here.


# class ListView(View):
#     paginate_by=2
    
#     def get(self,request,category_slug=None):
#         blogs=Blog.objects.filter(available=True)
#         categories=Category.objects.filter(is_sub=False)
#         if category_slug:
#            category=Category.objects.filter(slug=category_slug) 
#            blogs=blogs.filter(category=category)
#         # paginator = Paginator(blogs, per_page=2)
#         # page_object = paginator.get_page(page)
#         return render(request,'blog_app/list.html',{'blogs':blogs,'categories':categories})


class BlogListView(ListView):
    template_name = 'blog_app/list.html'
    paginate_by = 2
   
    def get_context_data(self, *args , object_list = None ,category_slug=None, **kwargs):

        blogs = Blog.objects.filter(available=True)
        categories=Category.objects.filter(is_sub=False)
        if category_slug:
           category=Category.objects.filter(slug=category_slug)
           blogs=blogs.filter(category=category)
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context['categories'] = categories
        context['blogs'] = blogs
        # most_visit_news = News.objects.order_by('-visit_count').all()[:3]
        # latest_news = News.objects.order_by('-id').filter(active=True)[:3]
        # category=NewsCategory.objects.all()
        # socials= Social.objects.all()
        # context = super(NewsList,self).get_context_data(*args ,**kwargs)  
        # context['socials'] = socials
           
        # context[ 'most_visit'] = my_grouper(1, most_visit_news)
        # context[ 'latest_news'] =  my_grouper(3, latest_news)
        return context  
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)
    
    def get_queryset(self):
        return Blog.objects.get_active_blog()


class BlogDetailView(View):
    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        return render(request, 'blog_app/detail.html', {'blog':blog})

