from django.db import models
from django.contrib.auth import get_user_model
from eshop_products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders',verbose_name='نام کاربر')
    paid = models.BooleanField(default=False,verbose_name='پرداخت شده/نشده ')
    created = models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True,verbose_name='زمان اپدیت ')
    discount = models.IntegerField(blank=True, null=True, default=None,verbose_name='تخفیف ')

    class Meta:
        ordering = ('paid', '-updated')
        verbose_name = ' سفارش'
        verbose_name_plural = 'سفارش ها'

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total

    def get_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        p=total+35000
        return p
 
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items',verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='نام محصول ')
    price = models.IntegerField(verbose_name='قیمت ')
    quantity = models.IntegerField(default=1,verbose_name='تعداد ')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = ' جزئیات سفارش'
        verbose_name_plural = 'جزئیات سفارش ها' 

class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True,verbose_name='کد ')
    valid_from = models.DateTimeField(verbose_name='از زمان ')
    valid_to = models.DateTimeField(verbose_name='تا زمان ')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)],verbose_name='درصد تخفیف ')
    active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال ')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = ' کد تخفیف'
        verbose_name_plural = 'کدهای تخفیف'