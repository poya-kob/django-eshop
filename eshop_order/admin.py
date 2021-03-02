from django.contrib import admin

from .models import OrderDetail, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_paid']
    list_filter = ['is_paid']
    search_fields = ['__str__']

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
