from django.contrib import admin
import nested_admin

from .models import Image, Banniere

class ImageInline(nested_admin.NestedStackedInline):
    model = Image
    extra = 0

class BanniereAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Banniere, BanniereAdmin)
admin.site.register(Image)
#admin.site.register(Department)
