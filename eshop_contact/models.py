from django.db import models
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

# Create your models here.

class ContactUs(models.Model):
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    subject = models.CharField(max_length=200, verbose_name='عنوان پیام')
    text = models.TextField(verbose_name='متن پیام')
    created_on = models.DateTimeField(auto_now_add=True,verbose_name='زمان ')
    is_read = models.BooleanField(verbose_name='خوانده شده / نشده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های کاربران'
        ordering = ['created_on']

    def __str__(self):
        return self.subject

