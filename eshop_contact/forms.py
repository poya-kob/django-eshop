from django import forms
from django.core import validators
from utilities.BaseFormWithCaptia import FormWithCaptcha


class ContactUsForm(FormWithCaptcha):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید', 'class': 'form-control'}),
        validators=[validators.MaxLengthValidator(limit_value=150, message='لطفا حداکثر 150 کاراکتر وارد کنید')]

    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید', 'class': 'form-control'}),
        validators=[validators.MaxLengthValidator(limit_value=100, message='لطفا حداکثر 100 کاراکتر وارد کنید')]

    )
    subject = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={'placeholder': 'عنوان پیام خود را وارد کنید', 'class': 'form-control'}),
        validators=[validators.MaxLengthValidator(limit_value=200, message='لطفا حداکثر 200 کاراکتر وارد کنید')]

    )
    text = forms.CharField(
        label='متن پیام',
        widget=forms.TextInput(attrs={'placeholder': 'متن پیام خود را وارد کنید',
                                      'class': 'form-control', 'rows': "8"})

    )
