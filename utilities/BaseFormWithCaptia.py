from django import forms
from captcha.fields import ReCaptchaField, ReCaptchaV2Checkbox


# from captcha.widgets import ReCaptchaV2Checkbox


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(
        label='تصویر امنیتی',
        widget=ReCaptchaV2Checkbox(api_params={'hl': 'fa'}),
        error_messages="بر روی تصویر زیر کلیک کنید"
    )
