from django.contrib import admin

from eshop_contact.models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
    search_fields = ['email', 'text', 'subject']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactAdmin)
