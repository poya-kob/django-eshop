from django import forms
from django.core import validators


class CommentForm(forms.Form):
    title = forms.CharField(
        label="عنوان دیدگاه",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان دیدگاه خود را وارد کنید'}),
        validators=[
            validators.MaxLengthValidator(limit_value=150, message="تعداد کارکتر های وارد شده بیشتر از حد مجاز است")]
    )
    text = forms.CharField(
        label="متن دیدگاه",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن دیدگاه خود را وارد کنید'})
    )
