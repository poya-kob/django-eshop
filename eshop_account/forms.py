from django import forms
from django.core import validators
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'})

    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور خود را وارد کنید'}),
        label='رمز عبور'
    )


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
        validators=[validators.MaxLengthValidator(limit_value=15, message='لطفا حداکثر 15 کاراکتر وارد کنید.'),
                    validators.MinLengthValidator(limit_value=4, message='لطفا حداقل 4 کاراکتر وارد کنید.')]

    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید'}),
        validators=[validators.EmailValidator(message='لطفا ایمیل معتبر وارد کنید.')]

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور خود را وارد کنید'}),
        label='رمز عبور',
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='رمز عبور نمی تواند بیشتر از 20 کاراکتر باشد.'),
            validators.MinLengthValidator(limit_value=8, message='رمز عبور نمی تواند کمتر از 8 کاراکتر باشد.')]
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور خود را تکرار کنید'}),
        label='تکرار رمز عبور',
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='رمز عبور نمی تواند بیشتر از 20 کاراکتر باشد.'),
            validators.MinLengthValidator(limit_value=8, message='رمز عبور نمی تواند کمتر از 8 کاراکتر باشد.')]
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_user_exists = User.objects.filter(username=user_name).exists()
        if is_user_exists:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_user_exists = User.objects.filter(username=email).exists()
        if is_user_exists:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه عبور یکسان نیست')
        return password
