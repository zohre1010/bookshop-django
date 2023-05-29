from django import forms


class CartAddForm(forms.Form):
	quantity = forms.IntegerField(min_value=1,label='  تعداد ')


class CouponApplyForm(forms.Form):
	code = forms.CharField(widget=forms.TextInput,label='  کد تخفیف')
