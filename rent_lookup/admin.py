from django.contrib import admin
import nested_admin

from .models import Department, City, Residence, Ecole, Logement, Image

class CityInline(nested_admin.NestedTabularInline):
    model = City
    extra = 3

class ImageInline(nested_admin.NestedTabularInline):
    model = Image
    extra = 0

class LogementInline(nested_admin.NestedStackedInline):
    model = Logement
    extra = 0

class EcoleInline(nested_admin.NestedTabularInline):
    model = Ecole
    extra = 0

class DepartmentAdmin(nested_admin.NestedModelAdmin):
    inlines = [CityInline]

#class EcoleAdmin(nested_admin.NestedModelAdmin):
#    inlines = [GeoInline]


class ResidenceAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        EcoleInline,
        LogementInline,
        ImageInline,
    ]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(City)
admin.site.register(Residence, ResidenceAdmin)
#admin.site.register(Ecole, EcoleAdmin)
admin.site.register(Ecole)
admin.site.register(Logement)
admin.site.register(Image)
