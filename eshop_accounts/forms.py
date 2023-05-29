
from django import forms
from django.core import validators
from eshop_accounts.models import User


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
        label='نام'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='نام خانوادگی'
    )


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}), label='نام کاربری')

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه ی عبور'
    )

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     is_exists_user = User.objects.filter(username=username).exists()
    #     if not is_exists_user:
    #         raise forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام نکرده است')

    #     return username

class RegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(limit_value=20,
                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
            validators.MinLengthValidator(3, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='کلمه ی عبور'
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='تکرار کلمه ی عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')

        if len(email) > 30:
            raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 30 باشد')

        return email

    def clean_user_name(self):
        username = self.cleaned_data.get('username')
        is_exists_user_by_username = User.objects.filter(username=username).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')

        return username

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password



