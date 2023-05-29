from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q
from eshop_accounts.models import User
from jalali_date.fields import  SplitJalaliDateTimeField

# Create your models here.

class BlogManager(models.Manager):
    def get_active_blog(self):
        return self.get_queryset().filter(available=True)

    def get_blog_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, available=True)

    def get_by_id(self, blog_id):
        qs = self.get_queryset().filter(id=blog_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, available=True).distinct()
    

class Category(models.Model):
    name = models.CharField(max_length=64,verbose_name='نام')
    slug = models.SlugField(max_length=224, unique=True,verbose_name='نام در آدرس صفحه')
    is_sub = models.BooleanField(default=False,verbose_name='آیا زیر مجموعه است')
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,related_name='scategory', null=True, blank=True,verbose_name='زیر مجموعه ی ')
    available = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_filter', args=[self.slug,])


class Blog(models.Model):
    category = models.ManyToManyField(Category, related_name='blogs',verbose_name='دسته بندی')
    name = models.CharField(max_length=200,verbose_name='نام')
    slug = models.SlugField(max_length=200, unique=True,verbose_name='نام در آدرس صفحه')
    image = models.ImageField(verbose_name='تصویر شاخص')
    description = RichTextUploadingField(verbose_name='توضیحات')
    available = models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    created = SplitJalaliDateTimeField()
    writer= models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='نویسنده')


    objects = BlogManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_app:blog_detail', args=[self.slug,])
    
