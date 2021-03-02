from django.contrib import admin
from .models import tag


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'slug', 'timestamp', 'active']

    class Meta:
        model = tag


admin.site.register(tag, TagAdmin)
