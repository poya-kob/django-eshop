from django.contrib import admin
from .models import Product, ProductGallery, UserComment


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']

    class Meta:
        model = Product


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'active']
    list_filter = ['user']
    list_editable = ['active']

    class Meta:
        model = UserComment


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
admin.site.register(UserComment, CommentsAdmin)
