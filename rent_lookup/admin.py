from django.contrib import admin
import nested_admin

from .models import City, Residence, Ecole, Logement, Image, Categorie

class ImageInline(nested_admin.NestedTabularInline):
    model = Image
    extra = 1

class LogementInline(nested_admin.NestedStackedInline):
    model = Logement
    extra = 0

class EcoleInline(nested_admin.NestedStackedInline):
    model = Ecole
    extra = 0

class ResidenceAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        EcoleInline,
        LogementInline,
        ImageInline,
    ]


#admin.site.register(Department)
admin.site.register(City)
admin.site.register(Residence, ResidenceAdmin)
admin.site.register(Categorie)
admin.site.register(Ecole)
admin.site.register(Logement)
admin.site.register(Image)
