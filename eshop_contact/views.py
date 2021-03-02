from django.shortcuts import render
from .forms import ContactUsForm
from .models import ContactUs
from eshop_setting.models import Setting


def contact_page(request):
    contact_form = ContactUsForm(request.POST or None)
    setting = Setting.objects.last()
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, email=email,
                                 subject=subject, text=text)
        # todo:show user a successful message
        contact_form = ContactUsForm()
    context = {
        'setting': setting,
        'contact_form': contact_form
    }
    return render(request, 'contact-us/contact_us_page.html', context)
