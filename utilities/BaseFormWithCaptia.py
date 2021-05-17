from django import forms
from captcha.fields import ReCaptchaField, ReCaptchaV2Checkbox


# from captcha.widgets import ReCaptchaV2Checkbox


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(
        label='تصویر امنیتی',
        widget=ReCaptchaV2Checkbox(api_params={
            'hl': 'fa'
        }),
        error_messages={"required": "لطفا بر روی من ربات نیستم کلیک کنید"}
    )
